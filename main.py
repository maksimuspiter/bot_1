from time import time

import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ Кит-бот от Максима!\n"
                        "Отправь мне /kit, а я тебе отправлю котика.")


# @dp.message_handler()
# async def echo(message: types.Message):
#     url = 'https://loremflickr.com/320/240'
#
#     await message.answer(message.text)


# async def send_photo(call: types.CallbackQuery):
#     photo = '1.jpg'
#     await call.message.answer_photo(photo)

@dp.message_handler(commands=['kit'])
async def sendphoto(msg):
    # photo = open('1.jpg', "rb")
    img = requests.get('https://loremflickr.com/320/240', allow_redirects=True).url
    await bot.send_photo(msg.from_user.id, img)


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def save_img():
    url = 'https://loremflickr.com/320/240'

    for i in range(2):
        write_file(get_file(url))
        print('Processed', i)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    # img = requests.get('https://loremflickr.com/320/240', allow_redirects=True)
    # print(img.url)
