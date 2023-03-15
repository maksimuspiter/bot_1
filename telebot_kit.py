import asyncio

import requests
from bs4 import BeautifulSoup
from telebot.async_telebot import AsyncTeleBot
from telebot import types

API_TOKEN = '5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs'

bot = AsyncTeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🐱кит")
    btn2 = types.KeyboardButton("анекдот")
    markup.add(btn1, btn2)
    await bot.reply_to(message, "Hi there, I am EchoBot", reply_markup=markup)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def send(message):
    if message.text == "🐱кит":
        img = requests.get('https://loremflickr.com/320/240', allow_redirects=True).url
        # await bot.reply_to(message, img)
        await bot.send_photo(message.from_user.id, img)
    elif message.text == "анекдот":

        url = 'http://www.RzhuNeMogu.ru/Widzh/WidzhRNM.aspx?type=1&callback=onSuccess'
        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'lxml')
        soup = str(soup)
        print(soup)
        new = soup[(soup.index('{"result":') + 11): (soup.index('</p><p><a'))]
        while '<br' in new:
            new = new.replace('<br>', '')
            new = new.replace('<br/>', '')

        await bot.send_message(message.from_user.id, new)


if __name__ == '__main__':
    asyncio.run(bot.polling())
