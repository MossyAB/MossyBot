#MossyBot by MossyAB
#Version 1.0

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time

bot = commands.Bot(command_prefix="%")

@bot.event
async def on_ready():
    print("Online")
    print("I am running on " + bot.user.name)
    print("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s infomation".format(user.name), color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="Server's Info", color=0x00ff00)
    embed.set_author(name="MossyAB")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.event
async def on_message(message):
    if message.content.upper().startswith('%SAY'):
        args = message.content.split(" ")
        await bot.send_message(message.channel, "%s" % (" ".join(args[1:])))


bot.run("NTA2MTM5ODI4NjE4OTE5OTM4.Drdzuw.0pzGB0mSSskUt3sfPfGIkuzEMng")
