import discord
import asyncio
import BEdevice
import os

from discord.ext import bridge
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv()
do_sleep = True if os.getenv("DO_SLEEP").lower() == 'true' else False
CHECK_PERIOD = 10 # amount of time (minutes) messages are considered when checking for join command

class PyCordBot(bridge.Bot):
    TOKEN = os.getenv("DISCORD_TOKEN")
    intents = discord.Intents.all()

client = PyCordBot(intents=PyCordBot.intents, command_prefix="!")

async def main_bot():
    print("Bot is starting...")
    await client.start(PyCordBot().TOKEN)

@client.listen()
async def on_ready():
    print(f"Logged on as {client.user.name}")
    await check_messages()

async def check_messages():   
    channel = client.get_channel(int(os.getenv("CHANNEL_ID"))) 
    async for message in channel.history(limit=100, after=datetime.now()-timedelta(minutes=CHECK_PERIOD), oldest_first=False):
        if '!join' in message.content:
            split_parts = message.content.split(" ", 2)
            if len(split_parts) >= 2 and split_parts[0] == "!join":
                arg = split_parts[1]
                await message.reply(f"launching Bleeding Edge... Standby this will take about {BEdevice.LOGIN_TIME + BEdevice.LOAD_TIME} seconds")
                BEdevice.join_game(arg)
                await channel.send(f"I am searching for \"{arg}\". you have {BEdevice.TIME_LIMIT} seconds to start the match")
                BEdevice.queue_expire()
                await channel.send("I have logged off enjoy the match!")
                await client.close()
                return
            else:
                await message.reply("invalid format use !join [code]")
    await client.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(main_bot()))
    if do_sleep:
        BEdevice.enter_sleep()