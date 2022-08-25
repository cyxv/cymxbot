from disnake.ext import commands
import disnake
import time

token = None
with open("token.txt") as f:
    token = f.read()

timerStart = time.time()

intents = disnake.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="c!", intents=intents)

extensions = ["cogs.general", "cogs.fun", "cogs.owner", "cogs.errorhandler", "jishaku"]

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
