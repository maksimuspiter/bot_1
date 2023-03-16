import time
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
TOKEN = '5896308515:AAGZwJtgI1OZ_KlMNEzxWbjLT4v2KOlAlVs'
MSG = 'Hi!{}'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_ful_name = message.from_user.full_name
    user_name = message.from_user.username
    logging.info(f'{user_id=} {user_ful_name=} {time.asctime()}')

    await message.reply(f"Hello, {user_ful_name}!")

    for i in range(10):
        time.sleep(2)

        await bot.send_message(user_id, MSG.format(user_name))


if __name__ == '__main__':
    executor.start_polling(dp)
