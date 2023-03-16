import json

import requests
from bs4 import BeautifulSoup
from telebot import types
from datetime import datetime


def create_start_btn():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("pictures")
    btn2 = types.KeyboardButton("😀анекдот")
    btn3 = types.KeyboardButton("interesting_fact_for_data")
    kb.add(btn1, btn2, btn3)
    return kb


def create_pictures_btns():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_cat = types.KeyboardButton("🐱cat")
    btn_dog = types.KeyboardButton("🐶dog")
    # my_option = types.KeyboardButton("my_option")
    return_back = types.KeyboardButton("return")
    kb.add(btn_cat, btn_dog)
    kb.add(return_back)

    return kb


async def send_photo(path, bot, img):
    img = requests.get(f'https://loremflickr.com/320/240/{img}', allow_redirects=True).url
    await bot.send_photo(path, img)


def get_joke():
    url = 'http://www.RzhuNeMogu.ru/Widzh/WidzhRNM.aspx?type=1&callback=onSuccess'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')
    soup = str(soup)
    new = soup[(soup.index('{"result":') + 11): (soup.index('</p><p><a'))]
    while '<br' in new:
        new = new.replace('<br>', '')
        new = new.replace('<br/>', '')
    return new


async def send_welcome_message(message, bot):
    markup = create_start_btn()
    await bot.send_message(message.from_user.id,
                           f"Hi {message.chat.first_name} , I am TestBot.\n"
                           f"I can show you some pictures with cats and dogs.\n"
                           f"I can tell you interesting number facts.",
                           reply_markup=markup)


def get_fact(number='random'):
    answer = requests.get(f'http://numbersapi.com/{number}/year?json')
    data = json.loads(answer.text).get('text', 'default')
    return data
