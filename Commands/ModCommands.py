import Commands.Utils as utils
import discord
import Storage.DatabaseContext as DatabaseContext
import logging

# TODO Insert Info Logs into Commands

class ModCommands():

    def __init__(self):
        return
        
    async def clear(self, message):
        channel = message.channel
        number = utils.get_message_after_command(message)
        deletedMessages = await channel.purge(limit = int(number))
        await channel.send('{} mensagens deletadas.'.format(len(deletedMessages)))
        return

    async def warn(self, server_id, user, message):
        channel = message.channel
        user_id = user.id
        database_context = DatabaseContext.DatabaseContext()
        warns = database_context.insert_or_update_warns(server_id, user_id)

        if warns % 3 != 0:
            await channel.send('Usuário {} tomou seu {} warn.'.format(user.mention, warns))
        else:
            await channel.send('Usuário {} banido com {} warnings.'.format(user.mention, warns))
            await message.guild.ban(user)

        return
    
    async def check_warns(self, user, server_id, channel):
        database_context = DatabaseContext.DatabaseContext()
        user_id = user.id
        warns = database_context.get_warns_by_user_id(user_id, server_id)
        await channel.send('Usuário {} tem {} warns.'.format(user.mention, warns))
        return 
    
    async def clear_warns(self, user, server_id, channel):
        database_context = DatabaseContext.DatabaseContext()
        user_id = user.id
        occurrences = database_context.clear_warns(user_id, server_id)
        if occurrences == 0:
            await channel.send('O usuário {} não tem warns registrados.'.format(user.mention))
        else:
            await channel.send('Os warns do usuário {} foram resetados.'.format(user.mention))
        return 

    async def get_user_info(self, message):
        # TODO complete this method
        channel = message.channel
        tagged = utils.check_if_tagged(message)
        embed=discord.Embed(title="User info", description="This is discord infos")
        if tagged == None:
            # Message author info
            user = message.author
            embed.add_field(name="Created at", value=user.created_at, inline=False)
            await channel.send(embed = embed)
            return
        # Tagged info
        user = tagged
        embed.add_field(name="Field 2 Title", value="Tagged!"+tagged, inline=False)
        await channel.send(embed = embed)
        return

