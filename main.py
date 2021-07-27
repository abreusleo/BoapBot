import discord
import logging

class MyClient(discord.Client):
    async def on_ready(self):
        # TODO Check if this is the best way to log something
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
        logging.info('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('NDQ2MTI1MzE2MzY5Mjg1MTIw.WvuMlA.CkKirbpz0bxq2tkqq40UE6h_oU0')