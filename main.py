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

    ModCommands = modCommands.ModCommands()
    ConfigCommands = configCommands.ConfigCommands()

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
        content = message.content
        author = message.author

        is_admin = author.top_role.permissions.administrator

        commandPrefix, self.prefix_cache = utils.update_cache(server_id, self.prefix_cache, os)
        logging.info(commandPrefix)
        logging.info(self.prefix_cache)
        try:
            if content.startswith(commandPrefix + 'clear'):
                await self.ModCommands.clear(message)

            elif content.startswith(commandPrefix + 'prefix'):
                commandPrefix = await self.ConfigCommands.change_prefix(message)
                self.prefix_cache[server_id] = commandPrefix
            
            elif content.startswith(commandPrefix + 'warn') and is_admin:
                warned_user = message.mentions[0].id
                user = await client.fetch_user(warned_user)
                await self.ModCommands.warn(server_id, user, message)
            
            elif content.startswith(commandPrefix + 'check') and is_admin:
                mentioned_user = message.mentions[0].id
                user = await client.fetch_user(mentioned_user)
                logging.info(mentioned_user)
                await self.ModCommands.check_warns(user, server_id, channel)

            elif content.startswith(commandPrefix + 'status'):
                await client.change_presence(activity=discord.Streaming(name="Boap Bot", url="https://www.twitch.tv/SugaredBeast"))
                await channel.purge(limit = 1)

        except:
            await self.bot_error(content.split()[0], channel)

client = MyClient()
TOKEN = os.getenv('DISCORD_TOKEN') # Get Token from .env file
client.run(TOKEN)