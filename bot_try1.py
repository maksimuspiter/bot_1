from telebot import types

import telebot

bot = telebot.TeleBot('5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs')


# @bot.message_handler(commands=['start'])
@bot.message_handler(chat_types=['private'], content_types=['text'], commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '1')


@bot.message_handler(chat_types=['group'], content_types=['text'], commands=['hello'])
def start(message):
    bot.send_message(message.chat.id, '2')


def create_start_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🐱кот")
    btn2 = types.KeyboardButton("😀анекдот")
    markup.add(btn1, btn2)
    return markup


@bot.message_handler(chat_types=['group'], content_types=['text'], commands=['start'])
def send_welcome_message(message):
    markup = create_start_btn()
    bot.send_message(message.chat.id, f"Hi, I am TestBot", reply_markup=markup)


@bot.message_handler(regexp=r'[0-9]')
def start(message):
    bot.send_message(message.chat.id, 'reg')


@bot.message_handler(func=lambda x: True)
def start(message):
    bot.send_message(message.chat.id, 'all right')


if __name__ == '__main__':
    bot.polling()
