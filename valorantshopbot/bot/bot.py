from typing import Final

import asyncio
import os
import sys
import traceback

from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ext.commands import ExtensionFailed, ExtensionNotFound, NoEntryPointError

bot_cogs = ['cogs.util']

# load token from env
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot setup
BOT_PREFIX = '!'

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready(self) -> None:
    print(f'{self.user} is now running.')

async def load_cogs():
    for cog in bot_cogs:
        try:
            await bot.load_extension(cog)
        except (
                ExtensionNotFound,
                NoEntryPointError,
                ExtensionFailed,
        ):
            print(f'Failed to load cog {cog}.', file=sys.stderr)
            traceback.print_exc()

async def run_bot() -> None:
    async with bot:
        await load_cogs()
        await bot.start(token=TOKEN)


if __name__ == '__main__':
    asyncio.run(run_bot())
