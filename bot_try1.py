from telebot import types
from time import sleep

import telebot
from telebot import types

bot = telebot.TeleBot('5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs')


# @bot.message_handler(commands=['start'])


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton(text='Button 1')
    btn2 = types.KeyboardButton(text='Button 2')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, '1', reply_markup=kb)


if __name__ == '__main__':
    bot.polling()
