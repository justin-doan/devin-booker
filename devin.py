# Devin is a discord bot that sends a motivational quote as well as other
# useful information every morning
# Is the sibling program to booker, a program that automatically books a UoL activity in the morning

from nextcord import Intents
from nextcord.ext import commands

import datetime, asyncio
import os 
from helper import get_random_quote

intents = Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix='!', intents=intents)

#!hi

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')


async def schedule_daily_quote(used_quotes):
    now = datetime.datetime.now()
    then = now.replace(hour=8, minute=0, second=0, microsecond=0)
    if now > then:
        then += datetime.timedelta(days=1)
    wait_time = (then - now).total_seconds()
    await asyncio.sleep(wait_time)
    channel = bot.get_channel(1096388182783836170)
    quote = get_random_quote("quotes.txt")
    quote = f"This is the quote of the day: {quote}"
    message = f"Good morning <@{386321709717782529}>!"
    await channel.send(message)
    await asyncio.sleep(1)
    await channel.send(quote)


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    loop = asyncio.get_event_loop()
    while True:
        loop.create_task(schedule_daily_quote(loop))
        await asyncio.sleep(86400)  # Wait for 24 hours
    loop.close()

if __name__ == '__main__':
    bot.run(os.environ['DISCORD_TOKEN'])