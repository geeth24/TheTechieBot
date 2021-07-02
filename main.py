import discord
import os
from discord.ext import commands
import string
from random import choice
from better_profanity import profanity

bot = commands.Bot(command_prefix='$')

character = string.ascii_letters + string.digits


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('The Techie'))
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    randomizer = "".join(choice(character) for x in range(6)) + "-" + "".join(choice(character) for x in range(6))
    randomizer = randomizer + randomizer
    profanity.load_censor_words()
    # For Bad Words
    if message.author == bot.user:
        return

    if 'fuck' in message.content:
        await message.delete()
        censored_text = profanity.censor(message.content)
        await message.channel.send("Stop cussing you bum " + message.author.mention + "!")
        await message.channel.send(message.author.mention + " said " + censored_text)

    if message.author == bot.user:
        return

    if message.content.startswith('pass'):
        await message.channel.send("Please Check Your Dms " + message.author.mention)
        await message.author.send(f"```{randomizer}```")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')


bot.run(os.getenv('TOKEN'))
