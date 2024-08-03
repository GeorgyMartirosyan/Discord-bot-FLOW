import disnake
import config

from disnake.ext import commands


bot = commands.Bot()


@bot.event
async def on_ready():
    print("Bot is running!")

bot.load_extension("cogs.ping")
bot.load_extension("cogs.server_info")

bot.run(config.TOKEN)
