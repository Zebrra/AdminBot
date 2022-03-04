#! /usr/bin/python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import traceback
import sys
import aiosqlite
import os
import json
import datetime
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv('config/.env'))

def get_prefix(bot, message):
    with open("config/prefixes.json", "r") as f:
        prefixes = json.load(f)

    try:
        pre = prefixes[str(message.guild.id)]
    except:
        prefixes[str(message.guild.id)] = "!"
        with open("config/prefixes.json", "w") as f:
            json.dump(prefixes, f)
        pre = prefixes[str(message.guild.id)]
    return pre

bot = commands.Bot(command_prefix= get_prefix, intents = discord.Intents.all())
bot.remove_command('help')

async def find_prefix():
    guild = bot.get_guild(int(os.environ['GUILD_ID']))

    with open('config/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    try:
        pre = prefixes[str(guild.id)]
    except:
        prefixes[str(guild.id)] = "!"
        with open("config/prefixes.json", "w") as f:
            json.dump(prefixes, f)
        pre = prefixes[str(guild.id)]

    print(f"Logged in as {bot.user}")
    return await bot.change_presence(activity= discord.Game(name= f"{pre}help"))

@bot.event
async def on_ready():

    main = await aiosqlite.connect('config/main.sqlite')
    cursor = await main.cursor()

    await cursor.execute('''
        CREATE TABLE IF NOT EXISTS warn(
            guild_id INTEGER,
            user_id INTEGER,
            user_name TEXT,
            reason TEXT
        )
    ''')
    await main.commit()

    await cursor.close()
    await main.close()

    await find_prefix()

@bot.event
async def on_guild_join(guild):

    with open("config/prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "!"

    with open("config/prefixes.json", "w") as f:
        json.dump(prefixes,f)


initial_extensions = [
    'cogs.cog_aahelp',
    'cogs.cog_error',
    'cogs.cog_admin',
    'cogs.cog_info',
    'cogs.cog_embed',
    'cogs.cog_prefix'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}", file=sys.stderr)
            traceback.print_exc()

bot.run(os.environ['TOKEN'])