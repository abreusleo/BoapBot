async def bulk(message):
    channel = message.channel
    msg = message.content.split()
    deletedMessages = await channel.purge(limit = int(msg[1]))
    await channel.send('{} mensagens deletadas.'.format(len(deletedMessages)))