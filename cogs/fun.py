import requests
import disnake
from disnake.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_member = None

    @commands.command()
    async def inspire(self, ctx):
        url = requests.get("https://inspirobot.me/api?generate=true").content.decode("utf-8")
        await ctx.send(embed=disnake.Embed().set_image(url=url).set_footer(text="cymx bot"))

def setup(client):
    client.add_cog(Fun(client))
