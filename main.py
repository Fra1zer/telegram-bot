import telebot
from telebot import types
import info

token = '6379306935:AAE0TYPvoQysIQIQginClDrACOZWbSTFGJ0'

bot = telebot.TeleBot(token=token)


def hello_filter(message):
    hello = 'привет'
    return hello in message.text.lower()


def bye_filter(message):
    bye = 'пока'
    return bye in message.text.lower()


@bot.message_handler(content_types=['text'], func=hello_filter)
def say_hello(message):
    bot.send_message(message.chat.id, f"И тебе привет, {message.from_user.first_name}!")


@bot.message_handler(content_types=['text'], func=bye_filter)
def say_bye(message):
    bot.send_message(message.chat.id, f"Пока, {message.from_user.first_name}!")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, задохлик, напиши команду /help, чтобы узнать, что я могу')


@bot.message_handler(commands=['info'])
def start_message(message):
    bot.send_message(message.chat.id, info.description)


@bot.message_handler(commands=['contacts'])
def start_message(message):
    bot.send_message(message.chat.id, info.contacts)


@bot.message_handler(commands=['projects'])
def start_message(message):
    bot.send_message(message.chat.id, info.projects)


@bot.message_handler(content_types=["photo"])
def get_photo(message):
    mark = types.InlineKeyboardMarkup()
    bot.reply_to(message, 'Молодец, хорошая картинка', reply_markup=mark)


@bot.message_handler(commands=['help'])
def information_message(message):
    bot.send_message(message.chat.id, 'Вот список того, что я умею:\n'
                                      '1.По команде /start готов к работе\n'
                                      '2.По команде /help вывожу эту справку\n'
                                      '3.Отвечаю на сообщение "привет"\n'
                                      '4.Отвечаю на сообщение "пока"\n'
                                      '5.Все другие сообщения дублирую\n'
                                      '6.По команде /info вывожу информацию о создателе\n'
                                      '7.По команде /contacts вывожу контакты создателя\n'
                                      '8.По команде /projects вывожу контакты создателя\n'
                                      '9.Отвечаю на картинки')


@bot.message_handler(content_types=['text'])
def repeat_message(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
