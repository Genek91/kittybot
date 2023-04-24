import requests
from telegram import Bot

bot = Bot(token='6131962065:AAG8kZSpKYY3nTpD4Ep9ywKCAq26-bWhEFc')
URL = 'https://api.thecatapi.com/v1/images/search'  
response = requests.get(URL).json()
random_cat_url = response[0].get('url')
bot.send_photo(5199953370, random_cat_url)

print(response)

print(type(response))

print(len(response))

print(type(response[0]))
