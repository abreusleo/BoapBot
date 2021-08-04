from asyncio.windows_events import NULL
import Commands.Utils as utils
import discord
import logging

# TODO Insert Info Logs into Commands

async def clear(message):
    channel = message.channel
    number = utils.get_message_after_command(message)
    deletedMessages = await channel.purge(limit = int(number))
    await channel.send('{} mensagens deletadas.'.format(len(deletedMessages)))

    return

async def get_user_info(message):
    channel = message.channel
    tagged = utils.check_if_tagged(message)
    embed=discord.Embed(title="User info", description="This is discord infos")
    if tagged == NULL:
        # Info do usuario que enviou o comando
        user = message.author
        embed.add_field(name="Created at", value=user.created_at, inline=False)
        await channel.send(embed = embed)
        return
    # Info do marcado
    user = tagged
    embed.add_field(name="Field 2 Title", value="Tagged!"+tagged, inline=False)
    await channel.send(embed = embed)
    return

