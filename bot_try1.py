from telebot import types
from time import sleep

import telebot

bot = telebot.TeleBot('5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs')


# @bot.message_handler(commands=['start'])


@bot.message_handler(commands=['start'])
def start(message):
    mess1 = bot.send_message(message.chat.id, '_all_ right')
    sleep(1)
    bot.edit_message_text(chat_id=message.chat.id, message_id=mess1.id, text='ass')


if __name__ == '__main__':
    bot.polling()
