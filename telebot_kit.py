import asyncio
import requests
from bs4 import BeautifulSoup
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from datetime import datetime

API_TOKEN = '5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs'

bot = AsyncTeleBot(API_TOKEN)


def create_start_btn():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("pictures")
    btn2 = types.KeyboardButton("😀анекдот")
    kb.add(btn1, btn2)
    return kb


def create_pictures_btns():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_cat = types.KeyboardButton("🐱cat")
    btn_dog = types.KeyboardButton("🐶dog")
    my_option = types.KeyboardButton("my_option")
    return_back = types.KeyboardButton("return")
    kb.add(btn_cat, btn_dog, my_option, return_back)
    return kb


async def send_photo(message, img):
    img = requests.get(f'https://loremflickr.com/320/240/{img}', allow_redirects=True).url
    await bot.send_photo(message.from_user.id, img)


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


async def send_welcome_message(message):
    markup = create_start_btn()
    await bot.send_message(message.from_user.id,
                           f"Hi {message.chat.first_name} , I am TestBot",
                           reply_markup=markup)


@bot.message_handler(commands=['help', 'start'])
async def first(message):
    await send_welcome_message(message)


@bot.message_handler(content_types=['text'])
async def send(message):
    match message.text:
        case "😀анекдот":
            joke = get_joke()
            await bot.send_message(message.from_user.id, joke)

        case 'pictures':
            markup = create_pictures_btns()
            await bot.send_message(message.from_user.id,
                                   'Check option',
                                   reply_markup=markup)
        case "🐱cat":
            await send_photo(message, 'cat')
        case "🐶dog":
            await send_photo(message, 'dog')
        case 'return_back':
            await send_welcome_message(message)

        case _:
            await send_welcome_message(message)
    # test
    if message.chat.id != 1712321379:
        mess = f'chat.id: {message.chat.id}, name: {message.chat.first_name}, time:{datetime.now()}'
        await bot.send_message(1712321379, mess)


if __name__ == '__main__':
    asyncio.run(bot.polling())
