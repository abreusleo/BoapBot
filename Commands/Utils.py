from asyncio.windows_events import NULL
import logging
import Storage.DatabaseContext as databaseContext

def get_message_after_command(message):
    msg = message.content.split()
    return msg[1]

def get_prefix_by_id(os, id):
    database_context = databaseContext.DatabaseContext(os)
    queryResult = database_context.get_prefix_by_id(id)
    print(queryResult)
    logging.info("Resultado da query {}".format(queryResult))

    return queryResult[0][1]

def check_if_tagged(message):
    msg = message.split()
    if(len(msg) > 1):
        return msg[1]
    return NULL