import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='techie')


@bot.event
async def on_ready():
    bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='The Techie Code & Produce'))
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('fuck') or message.content.startswith('shit') or message.content.startswith('bitch'):
        await message.delete()
        await message.channel.send(message.content)


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')


bot.run(os.getenv('TOKEN'))
