import disnake
from disnake.ext import commands


class Owner(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_member = None

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, msg):
        await ctx.send(msg)


def setup(client):
    client.add_cog(Owner(client))
