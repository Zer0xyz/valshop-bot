from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents,Client, Message
from responses import get_response

# load token from env
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# Message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    # private dm message with ? command

    # := is walrus operator for future reference
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        # TODO: should change this to logging instead of print in future
        print(e)

# Handle bot startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running.')

# Handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    # Make sure the bot doesn't respond to itself
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel} {username}: "{user_message}"')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()




