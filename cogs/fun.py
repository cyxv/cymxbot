import requests, json, random, os
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
        request = json.loads(requests.get("https://api.thecatapi.com/v1/images/search").content.decode("utf-8")) # example: [{'id': '<id>', 'url': 'https://cdn2.thecatapi.com/images/<id>.jpg', 'width': <width>, 'height': <height>}]
        await ctx.send(embed=disnake.Embed().set_image(url=request[0]["url"]).set_footer(text="cymx bot"))

    # still working on this, not complete
    @commands.command()
    async def pokemon(self, ctx, name):
        try:
            pokemon = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}").content.decode("utf-8"))
            entry = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{name.lower()}").content.decode("utf-8"))
        except:
            await ctx.send("Pokemon not found.")
            return
        name = entry["name"]
        emb = disnake.Embed(
            title = name[0].upper() + name[1:],
            description = "Here's all the info I could find:",
            color = 0xFFFFFF # idea: make this the color of the pokemon at some point
        )
        emb.add_field(name="ID", value=entry["id"])
        typelist = [x["type"]["name"] for x in pokemon["types"]]
        emb.add_field(name="Types", value=typelist)
        emb.add_field(name="Pokedex Entry", value=f"https://www.pokemon.com/us/pokedex/{name}")
        emb.set_image(url=f"http://play.pokemonshowdown.com/sprites/ani/{name}.gif")
        await ctx.send(embed=emb)

    @commands.command()
    async def capybara(self, ctx):
        request = json.loads(requests.get("https://api.capybara-api.xyz/v1/image/random").content.decode("utf-8"))
        await ctx.send(embed=disnake.Embed().set_image(url=request["image_urls"]["large"]).set_footer(text="cymx bot"))

    @commands.command()
    async def capyfact(self, ctx):
        request = None
        with open(os.path.join(os.path.dirname(__file__)) + "/data/capyfacts.json", "r") as f:
            request = json.loads(f.read())
        fact = random.choice(request)
        emb = disnake.Embed(
            title = "Fact",
            color = 0xFFFFFF,
            description = fact
        ).set_footer(text="cymx bot")
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Fun(client))
