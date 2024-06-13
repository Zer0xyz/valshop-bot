import discord
from discord.ext import commands

class Util(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def ping(self, ctx) -> None:
        bot_latency = round(self.bot.latency * 1000)

        await ctx.send(f"Pong! {bot_latency} ms.")

async def setup(bot) -> None:
    await bot.add_cog(Util(bot))