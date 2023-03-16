from telebot import types
from time import sleep
import requests
import json

import telebot
from telebot import types

bot = telebot.TeleBot('5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs')


def get_fact(number='random'):
    # answer = requests.get('http://numbersapi.com/125/year?json')
    answer = requests.get(f'http://numbersapi.com/{number}/year?json')
    print(json.loads(answer.text))
    data = json.loads(answer.text).get('text', 'default')
    return data


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='hello')


@bot.message_handler(regexp=r'[0-9]+')
def info(message):
    text = get_fact(message.text)
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling()
