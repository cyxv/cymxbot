import requests, json
import disnake
from disnake.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_member = None

    @commands.command()
    async def inspire(self, ctx):
        request = requests.get("https://inspirobot.me/api?generate=true").content.decode("utf-8")
        await ctx.send(embed=disnake.Embed().set_image(url=request).set_footer(text="cymx bot"))

    @commands.command()
    async def dog(self, ctx):
        request = json.loads(requests.get("https://dog.ceo/api/breeds/image/random").content.decode("utf-8"))
        await ctx.send(embed=disnake.Embed().set_image(url=request["message"]).set_footer(text="cymx bot"))

    @commands.command()
    async def cat(self, ctx):
        request = requests.get("https://api.thecatapi.com/v1/images/search").content.decode("utf-8")
        decoded = json.loads(request) # example: [{'id': '<id>', 'url': 'https://cdn2.thecatapi.com/images/<id>.jpg', 'width': <width>, 'height': <height>}]
        await ctx.send(embed=disnake.Embed().set_image(url=decoded[0]["url"]).set_footer(text="cymx bot"))

    # still working on this, not complete
    @commands.command()
    async def pokemon(self, ctx, name):
        pokemon = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").content.decode("utf-8"))
        entry = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{name}").content.decode("utf-8"))
        name = entry["name"]
        dex_id = entry["id"]
        types = pokemon["types"]
        sprite = f"http://play.pokemonshowdown.com/sprites/ani/{name}.gif"
        emb = disnake.Embed()


def setup(client):
    client.add_cog(Fun(client))
