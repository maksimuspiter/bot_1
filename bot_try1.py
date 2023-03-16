from telebot import types
from time import sleep

import telebot
from telebot import types

bot = telebot.TeleBot('5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id='@bot_test_stop', text='hello')
    # https://t.me/+WihmswUzO_JjMjZi
# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_data(callback):
#     if callback.data == 'btn1':
#         bot.send_message(callback.message.chat.id, 'You push btn1')
#     elif callback.data == 'btn2':
#         bot.send_message(callback.message.chat.id, 'You push btn2')


if __name__ == '__main__':
    bot.polling()
