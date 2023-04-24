import requests
from telegram import Bot

import os
from dotenv import load_dotenv


load_dotenv()


bot = Bot(token=os.getenv('TOKEN'))
URL = 'https://api.thecatapi.com/v1/images/search'  
response = requests.get(URL).json()
random_cat_url = response[0].get('url')
bot.send_photo(5199953370, random_cat_url)

print(response)

print(type(response))

print(len(response))

print(type(response[0]))
