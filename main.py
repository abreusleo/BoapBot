import os
import discord
import logging
import dotenv
import Commands.ModCommands as modCommands
import Commands.ConfigCommands as configCommands
import Commands.Utils as utils
class MyClient(discord.Client):
    dotenv.load_dotenv()
    LOG_LEVEL = os.getenv("LOG_LEVEL", "20")

    async def bot_error(self, command, channel):
        logging.error("{} error.".format(command))
        await channel.send('Comando inválido.')

    async def on_ready(self):
        # TODO 
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=int(self.LOG_LEVEL))
        logging.info('Boap is ready!')    

    async def on_message(self, message):
        if message.author == self.user:
            return

        channel = message.channel
        server_id = message.guild.id
        commandPrefix = utils.get_prefix_by_id(os, server_id)

        if message.content.startswith(commandPrefix + 'clear'):
            try:
                await modCommands.clear(message)
            except:
                await self.bot_error("Clear", channel)

        if message.content.startswith(commandPrefix + 'prefix'):
            try:
                await configCommands.change_prefix(message, os)
            except:
                await self.bot_error("Change prefix", channel)

client = MyClient()
TOKEN = os.getenv('DISCORD_TOKEN') # Get Token from .env file
client.run(TOKEN)