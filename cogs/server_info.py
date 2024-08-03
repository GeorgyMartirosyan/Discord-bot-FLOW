import disnake
from disnake.ext import commands


class ServerInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def server_info(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            f"# Информация о сервере"
            f"- **Название сервера:** {inter.guild.name}"
            f"- **Описание сервера:** {inter.guild.description}"
            f"- **Уровень верификации:** {inter.guild.verification_level}"
            f"- **AFK voice:** {inter.guild.afk_channel}")


def setup(bot: commands.Bot):
    bot.add_cog(ServerInfo(bot))
