import telebot

token = '6379306935:AAE0TYPvoQysIQIQginClDrACOZWbSTFGJ0'

bot = telebot.TeleBot(token=token)

chat_id = 693520821

def filter_hello(message):
    hello = "привет"
    return hello in message.text

@bot.message_handler(content_types=['text'], func = filter_hello)
def say_hello(message):
    bot.send_message(message.chat.id, "Привет!")

def filter_bye(message):
    bye = "пока"
    return bye in message.text

@bot.message_handler(content_types=['text'], func = filter_bye)
def say_bye(message):
    bot.send_message(message.chat.id, "Одиос!")

@bot.message_handler(content_types=['text'])
def repeat_message(message): # Функция для обработки сообщений
      bot.send_message(message.chat.id, message.text) # Отправка ответа

bot.polling()