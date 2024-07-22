import os
import disnake

from dotenv import load_dotenv
from disnake.ext import commands


load_dotenv('secret.env')

# Создание экземпляра класса commands.Bot() и присваивание его в "bot".
bot = commands.Bot()

# Когда бот будет готов, эта функция будет запущена.
@bot.event
async def on_ready():
    print("Bot is running!")

bot.run(os.getenv("API_KEY"))