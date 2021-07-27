import os
import discord
import logging
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        # TODO Check if this is the best way to log something
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)
        logging.info('Boap is ready!')

    async def on_message(self, message):
        logging.info('Message from {0.author}: {0.content}'.format(message)) #oi

load_dotenv()
client = MyClient()
TOKEN = os.getenv('DISCORD_TOKEN') # Get Token from .env file
client.run(TOKEN)