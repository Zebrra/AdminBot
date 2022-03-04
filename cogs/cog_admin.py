#! /usr/bin/python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import sqlite3
import os
import datetime

RULE_CHANNEL_ID = int(os.environ['RULE_CHANNEL_ID'])

async def create_muted_role(ctx):
    muted_role = await ctx.guild.create_role(name= "Muted",
                                            permissions= discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason= "Création du role Muted")

async def get_muted_role(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    return await create_muted_role(ctx)

class AdminCog(commands.Cog, name='AdminCog'):

    """Commandes d'administration"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages= True)
    async def mute(self, ctx, member: discord.Member, *, reason="Aucun"):

        """Mute un membre"""

        muted_role = await get_muted_role(ctx)
        await member.add_roles(muted_role, reason= reason)
        embed = discord.Embed(
            title= "**Mise sous silence**",
            description= "Un modérateur a frappé",
            color=0x2BC71F
        )
        embed.set_author(name= member.name, icon_url= member.avatar_url)
        embed.set_thumbnail(url= "https://upload.soshelpbot.com/uploads/1625133803.png")
        embed.add_field(name= "Membre mute", value= f"{member.mention}", inline= True)
        embed.add_field(name= "Motif", value= reason, inline= True)
        embed.add_field(name= "Modérateur", value= ctx.author.name, inline= True)

        await ctx.send(embed= embed)

    @commands.command()
    @commands.has_permissions(manage_messages= True)
    async def unmute(self, ctx, member: discord.Member, *, reason= "Aucun"):

        """Demute un membre"""

        muted_role = await get_muted_role(ctx)
        await member.remove_roles(muted_role, reason= reason)
        embed = discord.Embed(
            title= "**Révoquement du mute**",
            description= "Un modérateur s'est calmé",
            color=0x058AFF
        )
        embed.set_author(name= member.name, icon_url= member.avatar_url)
        embed.set_thumbnail(url= "https://upload.soshelpbot.com/uploads/1625133858.png")
        embed.add_field(name= "Membre unmute", value= member.mention, inline= True)
        embed.add_field(name= "Motif", value= reason, inline= True)
        embed.add_field(name= "Modérateur", value= ctx.author.name, inline= True)

        await ctx.send(embed= embed)

    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def ban(self, ctx, user: discord.User, *, reason= "Aucun"):

        """Permet de bannir un membre"""

        await ctx.guild.ban(user, reason= reason)
        embed = discord.Embed(
            title= "**Banissement**",
            description= "Un modérateur a frappé",
            color=0xCB2121
        )
        embed.set_author(name= user.name, icon_url= user.avatar_url)
        embed.set_thumbnail(url= "https://upload.soshelpbot.com/uploads/1625133898.png")
        embed.add_field(name= "Membre banni", value= user, inline= True)
        embed.add_field(name= "Motif", value= reason, inline= True)
        embed.add_field(name= "Modérateur", value= ctx.author.name, inline= True)
        
        await ctx.send(embed= embed)

    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def unban(self, ctx, id: int, *, reason= "Aucune"):

        """Permet de débannir un membre"""

        try:
            user = await self.bot.fetch_user(id)
            await ctx.guild.unban(user)

            embed = discord.Embed(
                title= "**Révoquement du ban**",
                description= "Un modérateur s'est calmé",
                color=0x058AFF
            )
            embed.set_author(name= user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(url= "https://upload.soshelpbot.com/uploads/1625133858.png")
            embed.add_field(name= "Membre banni", value= user, inline= True)
            embed.add_field(name= "Motif", value= reason, inline= True)
            embed.add_field(name= "Modérateur", value= ctx.author.name, inline= True)

            await ctx.send(embed= embed)
            return

        except:

            users = []
            banned_users = await ctx.guild.bans()
            for i in banned_users:
                users.append(str(f"> USER : **{i.user.name}#{i.user.discriminator}**, ID : **{i.user.id}**"))

            banned_list = "\n".join(users)
            not_found_embed = discord.Embed(
                title= "**Liste des bannis**",
                description= f"l'id ``{id}`` est introuvable voici les bannis du serveur..",
                color=0xFFDD05
            )
            not_found_embed.set_author(name= ctx.author.name, icon_url= ctx.author.avatar_url)
            not_found_embed.add_field(name="Pariats :", value= banned_list, inline= True)

            await ctx.send(embed= not_found_embed)
            return

    @commands.command()
    @commands.has_permissions(kick_members= True)
    async def show_ban(self, ctx):

        """Affiche la liste des bannis"""

        users = []

        banned_users = await ctx.guild.bans()
        for i in banned_users:
            users.append(str(f"> USER : **{i.user.name}#{i.user.discriminator}**, ID : **{i.user.id}**"))
        banned_list = "\n".join(users)

        if len(banned_list) == 0:
            banned_list = "Aucun bannis pour le moment"

        banned_embed = discord.Embed(
            title= "**Liste des bannis**",
            color=0xFFDD05
        )
        banned_embed.set_author(name= ctx.author.name, icon_url= ctx.author.avatar_url)
        banned_embed.add_field(name="Pariats :", value= banned_list, inline= True)

        await ctx.send(embed= banned_embed)


    @commands.command()
    @commands.has_permissions(kick_members= True)
    async def kick(self, ctx, user: discord.User, *, reason= "Aucun"):

        """Permet d'exclure temporairement un membre"""

        await ctx.guild.kick(user, reason= reason)
        embed = discord.Embed(
            title= "**Kick**",
            description= "Un modérateur a frappé",
            color=0xFF7E05
        )
        embed.set_author(name= user.name, icon_url= user.avatar_url)
        embed.set_thumbnail(url= "https://upload.soshelpbot.com/uploads/1625133958.png")
        embed.add_field(name= "Membre kick", value= user, inline= True)
        embed.add_field(name= "Motif", value= reason, inline= True)
        embed.add_field(name= "Modérateur", value= ctx.author.name, inline= True)

        await ctx.send(embed= embed)

    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def warn(self, ctx, member: discord.Member, *, reason= "Aucun"):

        """Pour avertir un membre"""

        main = sqlite3.connect('config/main.sqlite')
        cursor = main.cursor()
        
        warns = cursor.execute(f"SELECT guild_id, user_id, user_name, reason FROM warn WHERE guild_id = '{ctx.guild.id}' and user_id = '{member.id}'")
        result_warns = warns.fetchone()

        if result_warns is None:
            sql = ('INSERT INTO warn(guild_id, user_id, user_name, reason) VALUES(?,?,?,?)')
            val = (ctx.guild.id, member.id, str(member.name), reason)
        
        else:
            sql = ('INSERT INTO warn(guild_id, user_id, user_name, reason) VALUES(?,?,?,?)')
            val = (ctx.guild.id, member.id, str(member.name), reason)
        
        cursor.execute(sql, val)
        main.commit()

        db_count = cursor.execute(f"SELECT COUNT(user_id) FROM warn WHERE guild_id = '{ctx.guild.id}' and user_id = '{member.id}'")
        result_db_count = db_count.fetchone()


        warn_one = discord.utils.get(ctx.guild.roles, name="【⚠️】1er Avertissement")
        warn_two = discord.utils.get(ctx.guild.roles, name="【⚠️】2ème Avertissement")

        if warn_one is None:
            await ctx.guild.create_role(color=0xe2802a, name="【⚠️】1er Avertissement")
            warn_one = discord.utils.get(ctx.guild.roles, name="【⚠️】1er Avertissement")

        if warn_two is None:
            await ctx.guild.create_role(color=0xffd300, name="【⚠️】2ème Avertissement")
            warn_two = discord.utils.get(ctx.guild.roles, name="【⚠️】2ème Avertissement")


        channel = ctx.guild.get_channel(RULE_CHANNEL_ID)

        embed = discord.Embed(
            title = "Avertissement",
            description = f"{member.mention} fait attention à ce que tu fait sur le serveur,\n en cas d'oublie vas voir le {channel.mention}..",
            color=0xFF7E05
        )
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        embed.add_field(name="Nombre de warn :", value=f"Tu as {result_db_count[0]} warn", inline=True)
        embed.add_field(name="Motif du warn :", value=f"{reason}", inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

        if result_db_count[0] == 1:
            await member.add_roles(warn_one)
        if result_db_count[0] == 2:
            await member.add_roles(warn_two)
        if result_db_count[0] == 3:
            await ctx.guild.ban(member, reason= "S'est fait warn 3 fois")
            embed = discord.Embed(
            title= "**Banissement**",
            description= "Un modérateur a frappé",
            color=0xCB2121
            )
            embed.set_author(name= member.name, icon_url= member.avatar_url)
            embed.set_thumbnail(url= "https://upload.soshelpbot.com/uploads/1625133898.png")
            embed.add_field(name= "Membre banni", value= member, inline= True)
            embed.add_field(name= "Motif", value= "S'est fait warn 3 fois", inline= True)
            embed.add_field(name= "Modérateur", value= ctx.author.name, inline= True)
            
            await ctx.send(embed= embed)

        cursor.close()
        main.close()
        return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def show_warn(self, ctx, member: discord.Member=None):

        """Affiche la liste des warns."""
        
        embed = discord.Embed(
            title = "Liste des warns",
            color=0xFF7E05
        )

        main = sqlite3.connect('config/main.sqlite')
        cursor = main.cursor()

        if member is None:
            warns = cursor.execute(f"SELECT guild_id, user_id, user_name, reason FROM warn WHERE guild_id = '{ctx.guild.id}'")
            result_warns = warns.fetchall()
            if result_warns == []:
                embed.description = "Aucun enregistrement dans la base de données."
            else:
                for i in range(len(result_warns)):
                    member_name = self.bot.get_user(result_warns[i][1])
                    embed.add_field(name=f"Utilisateur {member_name} - ID : {result_warns[i][1]}", value=f"**Motif** :\n{result_warns[i][3]}", inline=False)
        else:
            warns = cursor.execute(f"SELECT guild_id, user_id, user_name, reason FROM warn WHERE guild_id = '{ctx.guild.id}' and user_id = '{member.id}'")
            result_warns = warns.fetchall()
            if result_warns == []:
                embed.description = f"Aucun enregistrement dans la base de données pour l'utilisateur {member.mention}"
            else:
                for i in range(len(result_warns)):
                    member_name = self.bot.get_user(result_warns[i][1])
                    embed.add_field(name=f"Utilisateur {member_name} - ID : {result_warns[i][1]}", value=f"**Motif** :\n{result_warns[i][3]}", inline=False)
                    
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
      
        cursor.close()
        main.close()
        return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, *, number:int=None):

        """Purge un nombre limité de message"""

        try:
            if number is None:
                await ctx.send('Entrer le nombre de message a purger')
                return
            else:
                deleted = await ctx.message.channel.purge(limit=number+1)
                await ctx.send(f"Messages purgés : **{len(deleted)}**")
                return
        except:
            await ctx.send("Impossible de purger les messages")
            return


def setup(bot):
    bot.add_cog(AdminCog(bot))
    print("The cog Admin is loaded")