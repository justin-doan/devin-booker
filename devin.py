# Devin is a discord bot that sends a motivational quote as well as other
# useful information every morning
# Is the sibling program to booker, a program that automatically books a UoL activity in the morning

from nextcord import Intents
from nextcord.ext import commands

import datetime, asyncio
import os 

intents = Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix='!', intents=intents)

#!hi

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')


async def schedule_daily_quote():
    now = datetime.datetime.now()
    then = now + datetime.timedelta(days=1)
    then = now.replace(hour=8, minute=0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)
    channel = bot.get_channel(1096388182783836170)
    await channel.send("Good.morning!")




@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    await schedule_daily_quote()

if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])