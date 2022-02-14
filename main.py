import os
import discord
import asyncio
from discord.ext import commands
token = os.getenv("token") 
bot = commands.Bot(command_prefix = "m!")
 
class BotData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None
 
        self.reaction_role = None
        self.reaction_message = None
 
botdata = BotData()
@bot.event
async def on_ready():
    print("Your bot is ready.")
 
 
@bot.command()
async def dm_all(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("'" + args + "' sent to: " + member.name)
 
            except:
                print("Couldn't send '" + args + "' to: " + member.name)
            await asyncio.sleep(60)
bot.run (token)
