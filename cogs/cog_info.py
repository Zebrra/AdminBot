#! /usr/bin/python3
# -*- coding: utf-8 -*-

from dis import dis
from tkinter import N
from unicodedata import name
import discord
from discord.ext import commands
from datetime import timezone

from more_itertools import value_chain


class InfoCog(commands.Cog, name='Info'):

    """Commandes d'informations"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def server_info(self, ctx):

        """Permet d'obtenir les infos relative au serveur"""

        owner = ctx.guild.owner

        users = []
        banned = await ctx.guild.bans()
        for i in banned:
            users.append(i)
        
        embed = discord.Embed(
            title=f"{ctx.guild.name}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Serveur crée le", value=ctx.guild.created_at.replace(tzinfo=timezone.utc).strftime('%d-%m-%Y'))
        embed.add_field(name="Propriétaire du serveur", value=f"{owner}", inline= False)
        embed.add_field(name="Région du serveur", value=ctx.guild.region, inline= True)
        embed.add_field(name="ID du server", value=ctx.guild.id, inline= False)
        embed.add_field(name="Nombre de membre", value=ctx.guild.member_count, inline= True)
        embed.set_footer(text=f"Nombre de bannis : {len(users)}")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


    @commands.command()
    async def user_info(self, ctx, member:discord.Member):

        """Affiche les informations d'un utilisateur."""

        embed = discord.Embed(
            color = 0x95d63c
        )
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.add_field(name="Création du compte :", value=member.created_at.replace(tzinfo=timezone.utc).strftime('%d-%m-%Y'))
        embed.add_field(name="À rejoins le serveur le :", value=member.joined_at.replace(tzinfo=timezone.utc).strftime('%d-%m-%Y'))
        embed.add_field(name="ID du membre : ", value=member.id)
        embed.add_field(name="Rôles du membre", value="\n".join([i.mention for i in member.roles[1:]]))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(InfoCog(bot))
    print("The cog Info is loaded")
