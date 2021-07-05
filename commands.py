import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('The Techie'))
    print('commands.py logged in as {0.user}'.format(bot))


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')


bot.run(os.getenv('TOKEN'))
