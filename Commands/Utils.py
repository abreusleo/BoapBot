import logging
import Storage.DatabaseContext as databaseContext

def get_message_after_command(message):
    msg = message.content.split()
    return msg[1]

def get_prefix_by_id(os, id):
    queryResult = databaseContext.get_prefix_by_id(os,id)
    logging.info("Resultado da query {}".format(queryResult))

    return queryResult[0][1]