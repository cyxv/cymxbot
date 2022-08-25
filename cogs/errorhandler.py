import disnake
from disnake.ext import commands

def errorEmbed(error):
	embed = disnake.Embed(
		title = "Error",
		description = error,
		color = 0xFFFFFF
	).set_footer(text="cymx bot")
	return embed

class ErrorHandler(commands.Cog):
	def __init__(self, client):
		self.bot = client
		self._last_member = None

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if hasattr(ctx.command, 'on_error'):
			return

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(embed=errorEmbed(f"Missing required argument. ({error.param.name})"))
		else:
			await ctx.send(embed=errorEmbed(error))


def setup(client):
    client.add_cog(ErrorHandler(client))
