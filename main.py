global token
with open("token.txt") as f:
    token = f.read()

import time
timerStart = time.time()

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

extensions = ["cogs.general", "jishaku"]

for extension in extensions:
  try:
    print('Attempting to load extension "{}"'.format(extension))
    client.load_extension(extension)
  except Exception as e:
    print('Failed to load extension "{}" ({})'.format(extension, e))
    
@client.event
async def on_ready():
  sec = round(time.time() - timerStart, 4)
  print("Bot loaded in {} seconds.".format(sec))
  
print("Starting bot...")
client.run(token)