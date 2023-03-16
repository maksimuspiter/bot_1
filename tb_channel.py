import asyncio
from telebot.async_telebot import AsyncTeleBot
from functions import create_pictures_btns, send_photo, get_joke, send_welcome_message

API_TOKEN = '5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs'

bot = AsyncTeleBot(API_TOKEN)
channel_id = '@bot_test_stop'


@bot.message_handler(content_types=['text'])
async def send(message):
    match message.text:
        case "😀анекдот":
            joke = get_joke()
            await bot.send_message(channel_id, joke)

        case 'pictures':
            markup = create_pictures_btns()
            await bot.send_message(message.from_user.id,
                                   'Check option',
                                   reply_markup=markup)
        case "🐱cat":
            await send_photo(channel_id, bot, 'cat')
        case "🐶dog":
            await send_photo(channel_id, bot, 'dog')
        case 'return_back':
            await send_welcome_message(message, bot)

        case _:
            await send_welcome_message(message, bot)


if __name__ == '__main__':
    asyncio.run(bot.polling())
