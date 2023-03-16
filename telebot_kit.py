import asyncio
from telebot.async_telebot import AsyncTeleBot
# from telebot import types
from datetime import datetime
from functions import create_pictures_btns, send_photo, get_joke, send_welcome_message, get_fact, create_start_btn

API_TOKEN = '5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs'

bot = AsyncTeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
async def first(message):
    await send_welcome_message(message, bot)


@bot.message_handler(regexp=r'[0-9]+')
async def info(message):
    text = get_fact(message.text)
    markup = create_start_btn()
    await bot.send_message(message.chat.id, text, reply_markup=markup)


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
            await send_photo(message.from_user.id, bot, 'cat')
        case "🐶dog":
            await send_photo(message.from_user.id, bot, 'dog')
        case 'interesting_fact_for_data':
            text = get_fact()
            await bot.send_message(message.chat.id, text)
        case 'return_back':
            await send_welcome_message(message, bot)

        # case 'my_option':
        #     sent = bot.reply_to(message.chat.id, 'Print your option')
        #     bot.register_next_step_handler
        case _:
            await send_welcome_message(message, bot)
    # test
    if message.chat.id != 1712321379:
        mess = f'chat.id: {message.chat.id}, name: {message.chat.first_name}, time:{datetime.now()}'
        await bot.send_message(1712321379, mess)


if __name__ == '__main__':
    asyncio.run(bot.polling())
