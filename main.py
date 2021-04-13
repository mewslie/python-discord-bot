import random
import configparser
# import discord
from discord.ext import commands, tasks

# Set bot and client
bot = commands.Bot(command_prefix='!')
# client = discord.Client()

# Get Discord Bot Token from the config file
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['dbbot']['discord_token']
GUILD = config['dbbot']['discord_channel']


@bot.event
async def on_ready():
    print('client ready')


# @bot.command()
# async def test(ctx):
#     await ctx.send('I heard you! {0}'.format(ctx.author))
#     # sends response if !test


@bot.event
async def on_message(message):
    # randomly sends a fortune in bot-channel when a message is sent
    if message.author != bot.user and message.channel.id == 831097025550483456 and len(message.content) > 3:
        fortune_list = [
            "Other things may change us, but we start and end with family.",
            "Good advice will be given to you, don't ignore it!",
            "In dreams and in life, nothing is impossible.",
            "Time enough for love.",
            "Many will travel to hear you speak.",
            "Many pleasurable and memorable adventures are in store for you.",
            "The best times of your life have not yet been lived.",
            "Love is the only medicine for a broken heart.",
            "Your wish is about to come true...",
            "Happy news is on the way to you.",
            "Your mentality is alert, practical and analytical.",
            "Give your love with a big hug.",
            "An investment in enthusiasm ought to start to pay off.",
            "You are a source of wisdom and strength to many others.",
            "Time enough for love.",
            "You will soon receive an offer you cannot refuse.",
            "Your patience will be rewarded sooner or later.",
            "Everything must experience a pain. Don't give up.",
            "Stop searching forever. Happiness is just next to you.",
            "You are a source of wisdom and strength to many others.",
            "Loves leisure and hates work. It is not a good phenomenon to carry on.",
        ]
        is_shown = random.choice(list(range(99)))  # 1% chance
        if is_shown == 50:
            response = "*A piece of paper floats down from the sky.*\nIt reads:\n> " + random.choice(fortune_list)
            await message.channel.send(response)


bot.run(TOKEN)



