import datetime

import disnake
from disnake.ext import commands
from config import Config

config = Config()


def info_contract(quantity: int, info: str):
    if quantity == 40000 or quantity == 43000 or quantity == 64000 and info == 'fish':
        name_contract = 'Дары моря I'
        activation_price = 2000
        family_price = 30000
        amount = 87000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 66000 or quantity == 70000 or quantity == 82000 and info == 'fish':
        name_contract = 'Дары моря II'
        activation_price = 2000
        family_price = config.family_price_fish
        amount = 114000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 122000 or quantity == 136000 or quantity == 138000 and info == 'fish':
        name_contract = 'Дары моря III'
        activation_price = 3000
        family_price = config.family_price_fish
        amount = 135000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 165000 or quantity == 136000 or quantity == 138000 and info == 'fish':
        name_contract = 'Дары моря IV'
        activation_price = 4000
        family_price = config.family_price_fish
        amount = 160000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 158000 or quantity == 163000 or quantity == 167000 and info == 'fish':
        name_contract = 'Дары моря V'
        activation_price = 5000
        family_price = config.family_price_fish
        amount = 182000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 204000 or quantity == 211000 or quantity == 193000 and info == 'fish':
        name_contract = 'Дары моря VI'
        activation_price = 6000
        family_price = config.family_price_fish
        amount = 210000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 213000 or quantity == 226000 or quantity == 251000 and info == 'fish':
        name_contract = 'Дары моря VII'
        activation_price = 7000
        family_price = config.family_price_fish
        amount = 240000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 243000 or quantity == 269000 or quantity == 291000 and info == 'fish':
        name_contract = 'Дары моря VIII'
        activation_price = 8000
        family_price = config.family_price_fish
        amount = 270000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 300 and info == 'metallurgy 1':
        name_contract = 'Металургия I | Железо'
        activation_price = 4000
        family_price = config.family_price_metallurgy
        amount = 72000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 150 and info == 'metallurgy 1':
        name_contract = 'Металургия I | Серебро'
        activation_price = 4000
        family_price = config.family_price_metallurgy
        amount = 90000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 75 and info == 'metallurgy 1':
        name_contract = 'Металургия I | Медь'
        activation_price = 4000
        family_price = config.family_price_metallurgy
        amount = 100000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 30 and info == 'metallurgy 1':
        name_contract = 'Металургия I | Олово'
        activation_price = 4000
        family_price = config.family_price_metallurgy
        amount = 110000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 15 and info == 'metallurgy 1':
        name_contract = 'Металургия I | Золото'
        activation_price = 4000
        family_price = config.family_price_metallurgy
        amount = 120000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 400 and info == 'metallurgy 2':
        name_contract = 'Металургия II | Железо'
        activation_price = 8000
        family_price = config.family_price_metallurgy
        amount = 93600
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 200 and info == 'metallurgy 2':
        name_contract = 'Металургия II | Серебро'
        activation_price = 8000
        family_price = config.family_price_metallurgy
        amount = 117000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 100 and info == 'metallurgy 2':
        name_contract = 'Металургия II | Медь'
        activation_price = 8000
        family_price = config.family_price_metallurgy
        amount = 128700
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 40 and info == 'metallurgy 2':
        name_contract = 'Металургия II | Олово'
        activation_price = 8000
        family_price = config.family_price_metallurgy
        amount = 140400
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 20 and info == 'metallurgy 2':
        name_contract = 'Металургия II | Золото'
        activation_price = 8000
        family_price = config.family_price_metallurgy
        amount = 156700
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 500 and info == 'metallurgy 3':
        name_contract = 'Металургия III | Железо'
        activation_price = 12000
        family_price = config.family_price_metallurgy
        amount = 121600
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 250 and info == 'metallurgy 3':
        name_contract = 'Металургия III | Серебро'
        activation_price = 12000
        family_price = config.family_price_metallurgy
        amount = 152100
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 125 and info == 'metallurgy 3':
        name_contract = 'Металургия III | Медь'
        activation_price = 12000
        family_price = config.family_price_metallurgy
        amount = 167300
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 50 and info == 'metallurgy 3':
        name_contract = 'Металургия III | Олово'
        activation_price = 12000
        family_price = config.family_price_metallurgy
        amount = 182500
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 25 and info == 'metallurgy 3':
        name_contract = 'Металургия III | Золото'
        activation_price = 12000
        family_price = config.family_price_metallurgy
        amount = 204000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 600 and info == 'metallurgy 4':
        name_contract = 'Металургия IV | Железо'
        activation_price = 16000
        family_price = config.family_price_metallurgy
        amount = 158000
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 300 and info == 'metallurgy 4':
        name_contract = 'Металургия IV | Серебро'
        activation_price = 16000
        family_price = config.family_price_metallurgy
        amount = 197700
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 150 and info == 'metallurgy 4':
        name_contract = 'Металургия IV | Медь'
        activation_price = 16000
        family_price = config.family_price_metallurgy
        amount = 217500
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 60 and info == 'metallurgy 4':
        name_contract = 'Металургия IV | Олово'
        activation_price = 16000
        family_price = config.family_price_metallurgy
        amount = 237200
        return [name_contract, activation_price, family_price, amount]
    elif quantity == 30 and info == 'metallurgy 4':
        name_contract = 'Металургия IV | Золото'
        activation_price = 16000
        family_price = config.family_price_metallurgy
        amount = 265000
        return [name_contract, activation_price, family_price, amount]
    else:
        name_contract = 'Error'
        activation_price = 0
        family_price = 0
        amount = 0
        return [name_contract, activation_price, family_price, amount]


def calculation(quantity: int, count_item: int, info: str):
    contract_name, activation_price, family_price, amount = info_contract(quantity, info)
    return count_item * (amount - activation_price - family_price) / quantity


class SalaryCalculator(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.answer = None
        self.bot = bot

    @commands.slash_command()
    async def embed(self, inter: disnake.ApplicationCommandInteraction, quantity: int, count_item: int, info: str):
        contract_name, activation_price, family_price, amount = info_contract(quantity, info)
        embed = disnake.Embed(
            title="Finance",
            description=contract_name,
            color=disnake.Colour.blue(),
            timestamp=datetime.datetime.now(),
        )

        embed.set_author(
            name=" ",
            url="https://discord.gg/pyBc772wYM",
            icon_url="https://static.vecteezy.com/system/resources/thumbnails/007/264/787/small/business-finance-"
                     "logo-template-illustration-free-vector.jpg",
        )
        embed.set_footer(
            text="by martirosyan",
            icon_url="https://static.vecteezy.com/system/resources/thumbnails/007/264/787/small/business-finance-logo-"
                     "template-illustration-free-vector.jpg",
        )

        # embed.set_thumbnail(url="https://disnake.dev/assets/disnake-logo.png")
        # embed.set_image(url="https://images.wsj.net/im-861258?size=1.5005861664712778&width=600&height=400")

        embed.add_field(name="Сумма которую вам выплатят:",
                        value=calculation(quantity, count_item, info),
                        inline=False
                        )

        await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(SalaryCalculator(bot))
