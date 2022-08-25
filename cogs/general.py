import disnake
from disnake.ext import commands

class General(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_member = None

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        emb = disnake.Embed(
            title = "Pong! :ping_pong:",
            description = f"Latency is {latency}ms.",
            color = 0xFFFFFF
        ).set_footer(text="cymx bot")
        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(General(client))
