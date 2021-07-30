import Storage.DatabaseContext as databaseContext
import logging

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
    
    try:
        databaseContext.insert_or_update_server_config(os, server_id, prefix)
        await channel.send('Prefixo {} armazenado.'.format(prefix))
        return prefix
    except:
        logging.error('Erro ao armazenar o prefixo escolhido.')
