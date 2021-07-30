import Storage.DatabaseContext as databaseContext
import Commands.Utils as utils
import logging



async def change_prefix(message, os):
    prefix = utils.get_message_after_command(message)
    channel = message.channel
    server_id = message.guild.id

    databaseContext.insert_or_update_server_config(os, server_id, prefix)
    logging.info('Prefixo {} armazenado para servidor {}'.format(prefix, server_id))
    
    await channel.send('Prefixo {} armazenado.'.format(prefix))
    
    return
