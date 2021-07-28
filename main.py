import os
import discord
import logging
import ModCommands as modCommands
import dotenv

def choose_command_prefix(prefixList, id):
    for el in prefixList:
        if el[0] == id:
            return el[1]
    return prefixList[0][1]

class MyClient(discord.Client):
    dotenv.load_dotenv()
    commandPrefix = os.getenv('DISCORD_COMMAND_PREFIX')

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

        if message.content.startswith(self.commandPrefix + 'bulk'):
            try:
                await modCommands.bulk(message)
            except:
                await self.bot_error("Bulk delete", channel)

client = MyClient()
TOKEN = os.getenv('DISCORD_TOKEN') # Get Token from .env file
client.run(TOKEN)