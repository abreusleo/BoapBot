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

    prefix_cache = {}

    async def bot_error(self, command, channel):
        logging.error("{} error.".format(command))
        await channel.send('Comando inválido.')

    async def on_ready(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=int(self.LOG_LEVEL))
        logging.info('Boap is ready!')    

    async def on_message(self, message):
        if message.author == self.user:
            return
        channel = message.channel
        server_id = message.guild.id
        if server_id not in self.prefix_cache:
            commandPrefix = utils.get_prefix_by_id(os, server_id)
            self.prefix_cache[server_id] = commandPrefix
        else:
            commandPrefix = self.prefix_cache[server_id]
            logging.info("Resultado da cache [({}, {})]".format(server_id, commandPrefix))

        if message.content.startswith(commandPrefix + 'clear'):
            try:
                await modCommands.clear(message)
            except:
                await self.bot_error("Clear", channel)

        if message.content.startswith(commandPrefix + 'prefix'):
            try:
                commandPrefix = await configCommands.change_prefix(message, os)
                self.prefix_cache[server_id] = commandPrefix
            except:
                await self.bot_error("Change prefix", channel)
        
        if message.content.startswith(commandPrefix + 'info'):
            try:
                await modCommands.get_user_info(message)
            except:
                await self.bot_error("Info", channel)
        
        if message.content.startswith(commandPrefix + 'warn'):
            try:
                warned_user = message.mentions[0].id
                user = await client.fetch_user(warned_user)
                await modCommands.warn(server_id, user, message, os)
            except:
                await self.bot_error("Warn", channel)

client = MyClient()
TOKEN = os.getenv('DISCORD_TOKEN') # Get Token from .env file
client.run(TOKEN)