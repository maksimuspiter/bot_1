import requests
from bs4 import BeautifulSoup
import re
from aiogram import Bot, Dispatcher, executor, types
import sicret_data

TOKEN = sicret_data.API_TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


def searcher():
    response = requests.get('https://www.youtube.com/results?search_query=witcher')
    soup = BeautifulSoup(response.content, 'html.parser')
    with open('test.html', 'w') as f:
        print(soup, file=f)



if __name__ == '__main__':
    # executor.start_polling(dp, skip_updates=True)
    searcher()
