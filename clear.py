import asyncio
import discord
from discord.ext import commands,tasks
from itertools import cycle


client = commands.Bot(command_prefix='.')
status = cycle(['football','chess'])
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello there!'))
    change_status.start()
    print("bot is ready")

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command(name='clear', help='this command will clear msgs')
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit = amount)

class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]
        
        if amount.isdigit() and unit in['s','m']:
            return (int(amount), unit)

        raise commands.BadArgument(message='Not a valid duration')



@client.command()
async def tempban(ctx , member : commands.MemberConverter, duration : DurationConverter ):
    multiplier = {'s':1,'m':60}
    amount, unit = duration
    await ctx.guild.ban(member)
    await ctx.send(f'{member} has been banned for {amount}{unit}.')
    await asyncio.sleep(amount * multiplier[unit])
    await ctx.guild.unban(member)

logging_channel = 951744640288194593

@client.event
async def on_message_delete(message):
    embed=discord.Embed(title="{} deleted a message".format(message.member.name), description="", color="Blue")
    embed.add_field(name= message.content ,value="This is the message that he has deleted", inline=True)
    channel=client.get_channel(951744640288194593)
    await channel.send(channel, embed=embed)


@client.command()
async def ban(ctx , member: commands.MemberConverter):
    await ctx.guild.ban(member)
    await ctx.send(f'{member} has been banned.')



client.run('OTUyMTc5NjIzODgwNDQ1OTUy.YiyQYA.mYuoGpzCN9VjnT7uy3TGdYyVIaQ')