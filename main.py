import os
import discord
import logging
import ModCommands as modCommands
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def bot_error(self, command, channel):
        logging.error("{} error.".format(command))
        await channel.send('Comando inválido.') 

    async def on_ready(self):
        # TODO Check if this is the best way to log something
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)
        logging.info('Boap is ready!')

    async def on_message(self, message):
        author = message.author
        channel = message.channel

        if message.author == self.user:
            return

        if message.content.startswith('!bulk'):
            try:
                await modCommands.bulk(message)
            except:
                await self.bot_error("Bulk delete", channel)

load_dotenv()
client = MyClient()
TOKEN = os.getenv('DISCORD_TOKEN') # Get Token from .env file
client.run(TOKEN)