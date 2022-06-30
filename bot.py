import hikari
import lightbulb
import discord
from discord.ext import commands


bot = lightbulb.BotApp(
                       token='OTUxNzk1MDA3MTUxNTYyNzcy.YisqLQ.XUNwUV0yBB7BcRNmdSqpzkrE6p8',
                       default_enabled_guilds=(951744640288194590)
                       )
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(content):
    print("bot has started")


@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Diwas bot is here')

@bot.command
@lightbulb.command('group', 'this is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def mygroup(ctx):
    pass

@mygroup.child
@lightbulb.command('subcommand','this is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand')

@bot.command
@lightbulb.option('num2','The Second Number',type=int)
@lightbulb.option('num1','The First Number',type=int)
@lightbulb.command('add','Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

@bot.command
@lightbulb.option('num1','The First Number',type=int)
@lightbulb.option('num2','The Second Number',type=int)
@lightbulb.command('substract','Substraction of two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def substract(ctx):
    await ctx.respond(ctx.options.num1 - ctx.options.num2)









bot.run()
