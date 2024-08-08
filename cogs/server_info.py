import disnake
from disnake.ext import commands


class ServerInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def server_info(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            f"# Информация о сервере"
            f"\n- **Название сервера:** {inter.guild.name}"
            f"\n- **Описание сервера:** {inter.guild.description}"
            f"\n- **Уровень верификации:** {inter.guild.verification_level}"
            f"\n- **AFK voice:** {inter.guild.afk_channel}")


def setup(bot: commands.Bot):
    bot.add_cog(ServerInfo(bot))
