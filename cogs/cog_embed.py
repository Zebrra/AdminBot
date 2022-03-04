#! /usr/bin/python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import datetime
import random

class EmbedCog(commands.Cog, name = "Embed"):

    """Créateur d'embeds"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def embeds(self, ctx, *, message):

        """Permet de formater un embed avec une couleur aléatoire. (Les images et les gif sont pris en compte.)"""
        await ctx.message.delete()
        embed = discord.Embed(
            colour=random.randint(0, 16777215),
        )
        embed.set_author(name= f"{ctx.author.name}", icon_url= f"{ctx.author.avatar_url}")
        embed.set_footer(text= f"{ctx.author.guild}", icon_url= f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()

        pict_ext = ['.jpg', '.jpeg', '.JPG', '.JPEG','.png', '.PNG', '.GIF', '.gif']
        try:
            for ext in pict_ext:
                if ctx.message.attachments[0].url.endswith(ext):
                    embed.set_image(url=ctx.message.attachments[0].url)
                    if message.content != None:
                        embed.description = message

        except:
            embed.description = message
            
        await ctx.send(embed= embed)

def setup(bot):
    bot.add_cog(EmbedCog(bot))
    print('The cog Embed is loaded')