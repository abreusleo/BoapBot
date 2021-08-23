from asyncio.windows_events import NULL
import logging
import Storage.DatabaseContext as databaseContext

def get_message_after_command(message):
    msg = message.content.split()

    return msg[1]

def get_prefix_by_id(os, id):
    database_context = databaseContext.DatabaseContext()

    queryResult = database_context.get_prefix_by_id(id)
    logging.info("Resultado da query {}".format(queryResult))

    return queryResult[0][1]

def check_if_tagged(message):
    msg = message.split()

    if(len(msg) > 1):
        return msg[1]
    return NULL

def update_cache(server_id, prefix_cache, os):
    if server_id not in prefix_cache:
        commandPrefix = get_prefix_by_id(os, server_id)
        prefix_cache[server_id] = commandPrefix
    else:
        commandPrefix = prefix_cache[server_id]
        logging.info("Resultado da cache [({}, {})]".format(server_id, commandPrefix))

    return commandPrefix, prefix_cache