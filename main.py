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
        content = message.content

        commandPrefix, self.prefix_cache = utils.update_cache(server_id, self.prefix_cache, os)

        try:
            if message.content.startswith(commandPrefix + 'clear'):
                await modCommands.clear(message)

            elif message.content.startswith(commandPrefix + 'prefix'):
                commandPrefix = await configCommands.change_prefix(message, os)
                self.prefix_cache[server_id] = commandPrefix
            
            # elif message.content.startswith(commandPrefix + 'info'):
            #     await modCommands.get_user_info(message)
            
            elif message.content.startswith(commandPrefix + 'warn'):
                warned_user = message.mentions[0].id
                user = await client.fetch_user(warned_user)
                await modCommands.warn(server_id, user, message, os)

            elif message.content.startswith(commandPrefix + 'status'):
                await client.change_presence(activity=discord.Streaming(name="Boap Bot", url="https://www.twitch.tv/SugaredBeast"))

        except:
            await self.bot_error(content.split()[0], channel)

client = MyClient()
TOKEN = os.getenv('DISCORD_TOKEN') # Get Token from .env file
client.run(TOKEN)