import Storage.DatabaseContext as databaseContext

# TODO Insert Info Logs into Commands

def get_message_after_command(message):
    msg = message.content.split()
    return msg[1]

async def clear(message):
    channel = message.channel
    number = get_message_after_command(message)
    deletedMessages = await channel.purge(limit = int(number))
    await channel.send('{} mensagens deletadas.'.format(len(deletedMessages)))

async def change_prefix(message, os):
    prefix = get_message_after_command(message)
    channel = message.channel
    server_id = message.guild.id
    
    databaseContext.insert_server_config(os, server_id, prefix)
    await channel.send('Prefixo armazenado.')
    
