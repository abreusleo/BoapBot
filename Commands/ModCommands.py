import Commands.Utils as utils
import discord
import Storage.DatabaseContext as DatabaseContext
import logging

# TODO Insert Info Logs into Commands

async def clear(message):
    channel = message.channel
    number = utils.get_message_after_command(message)
    deletedMessages = await channel.purge(limit = int(number))
    await channel.send('{} mensagens deletadas.'.format(len(deletedMessages)))

    return

async def warn(server_id, user, message, os):
    channel = message.channel
    user_id = user.id
    database_context = DatabaseContext.DatabaseContext(os)
    warns = database_context.insert_or_update_warns(server_id,user_id)
    if warns < 3:
        print(warns)
        await channel.send('Usuário {} tomou seu {} warn'.format(user.mention, warns))
    else:
        await channel.send('Usuário {} banido com {} warnings'.format(user.mention, warns))
        await message.guild.ban(user)   
    return

async def get_user_info(message):
    channel = message.channel
    tagged = utils.check_if_tagged(message)
    embed=discord.Embed(title="User info", description="This is discord infos")
    if tagged == None:
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

