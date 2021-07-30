import Storage.DatabaseContext as databaseContext
import Commands.Utils as utils
import logging

# TODO Insert Info Logs into Commands

async def clear(message):
    channel = message.channel
    number = utils.get_message_after_command(message)
    deletedMessages = await channel.purge(limit = int(number))
    await channel.send('{} mensagens deletadas.'.format(len(deletedMessages)))

    return

