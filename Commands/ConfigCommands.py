import Storage.DatabaseContext as DatabaseContext
import Commands.Utils as utils
import logging

class ConfigCommands():
    
    def __init__(self,os):
        self.os = os
        return
    
    async def change_prefix(self, message, os):
        prefix = utils.get_message_after_command(message)
        channel = message.channel
        server_id = message.guild.id

        database_context = DatabaseContext.DatabaseContext(os)
        database_context.insert_or_update_server_config(server_id, prefix)

        logging.info('Prefixo {} armazenado para servidor {}'.format(prefix, server_id))
        await channel.send('Prefixo {} armazenado.'.format(prefix))
        return
