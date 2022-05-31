#OTgwNjcwMzE4MjM2NTQxMDA5.Gjg2rI.NhT9u2qe5zIrj9xn96tJvRGoLtvziIGXWBFxKc

from inspect import Parameter
import discord
from discord.ext import commands

intents=discord.Intents.all()
intents.members=True

bot = commands.Bot(command_prefix="",intents=intents)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(981088759552540692)
    await channel.send(F"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(981088780423430194)
    await channel.send(F"{member} leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(F"{round(bot.latency*1000)} ms")

@bot.command()
async def goout(ctx):
    await ctx.send(F"幹喜哩靠杯炒三小")


bot.run("OTgwNjcwMzE4MjM2NTQxMDA5.Gjg2rI.NhT9u2qe5zIrj9xn96tJvRGoLtvziIGXWBFxKc")

