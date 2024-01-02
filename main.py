import json
import os

import telebot
from info import characters, questions, welcome_message
from telebot import types

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)


def load_user_data():
    with open("user_data.json", "r") as file:
        return json.load(file)


def save_user_data(user_data):
    with open("user_data.json", "w") as file:
        json.dump(user_data, file)


if os.path.exists("user_data.json"):
    user_data = load_user_data()
else:
    user_data = {}


@bot.message_handler(commands=["start"])
def start_survey(message):
    user_data[message.chat.id] = {character: 0 for character in characters}
    user_data[message.chat.id]["question_index"] = 0

    bot.send_message(message.chat.id, welcome_message)
    send_question(message.chat.id)

    save_user_data(user_data)


def send_question(chat_id):
    question_index = user_data[chat_id]["question_index"]

    question, options = questions[question_index]

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for text, _ in options:
        markup.add(text)
    bot.send_message(chat_id, question, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    if message.chat.id not in user_data:
        bot.send_message(
            message.chat.id,
            "Пожалуйста, начните анкету с помощью команды /start",
        )
        return

    chat_id = message.chat.id
    question_index = user_data[chat_id]["question_index"]
    _, options = questions[question_index]

    selected_option = None
    for option in options:
        if option[0] == message.text:
            selected_option = option[1]
            break
    if not selected_option:
        bot.send_message(
            chat_id, "Пожалуйста, выберите один из предложенных вариантов."
        )
        return

    for character, score in selected_option.items():
        user_data[chat_id][character] += score

    user_data[chat_id]["question_index"] += 1
    if user_data[chat_id]["question_index"] < len(questions):
        send_question(chat_id)
    else:
        send_result(chat_id)

    save_user_data(user_data)


def send_result(chat_id):
    scores = {
        character: score
        for character, score in user_data[chat_id].items()
        if character != "question_index"
    }

    max_character = max(scores, key=scores.get)

    description, image_name = characters[max_character]
    caption_message = f"Ваш тип мышления: {max_character}\n{description}"

    with open(image_name, "rb") as image:
        bot.send_photo(chat_id, image, caption=caption_message)

    del user_data[chat_id]

    save_user_data(user_data)


bot.polling(non_stop=True)
