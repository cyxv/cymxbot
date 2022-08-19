import discord
from discord.ext import commands

class General(commands.Cog):
  def __init__(self, client):
    self.bot = client
    self._last_member = None
    
  @commands.command()
  async def ping(self, ctx):
    latency = round(self.bot.latency * 1000)
    await ctx.send("Pong! Latency is {}ms.".format(latency)) 
    
  def setup(client):
    client.add_cog(General(client))