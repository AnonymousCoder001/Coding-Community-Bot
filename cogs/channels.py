import discord
import asyncio
from discord.ext import commands

class Help(commands.Cog, name = 'help'):

    def __init__ (self,bot):
        self.bot = bot
        self.bot.hp1 = False
        self.bot.hp2 = False
        self.bot.hp3 = False

    @commands.Cog.listener()
    async def on_message(self,message):
        cata = self.bot.get_channel(756195945854795927)
        back = self.bot.get_channel(755862487999447063)
        role = discord.utils.get(message.guild.roles, name = 'Helper')
        if message.author.guild_permissions.manage_messages == True:
            pass
        elif message.channel.id == 754710893538836480 and message.author.id != 755479510387916871:
            if self.bot.hp1 == True:
                pass
            else:
                embed = discord.Embed(title = f'You have just claimed {message.channel.name}.',
                 description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                embed.add_field(name = f'If you need someones attention: ', value = f"Ping {role.mention}, they would be happy to help.")
                await message.channel.send(embed = embed)
                cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                await message.author.add_roles(cool)
                await message.channel.edit(category = cata, sync_permissions = True)
                self.bot.hp1 = True
                await asyncio.sleep(900)
                await message.author.remove_roles(cool)
                await message.channel.edit(category = back)
                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                description = 'If you still have problems, just claim another help channel.', color = discord.Colour.from_rgb(255,221,170))
                await message.channel.send(embed = embed2)
                self.bot.hp1 = False
                
        elif message.channel.id == 754710998769991680 and message.author.id != 755479510387916871:
            if self.bot.hp2 == True:
                pass
            else:
                embed = discord.Embed(title = f'You have just claimed {message.channel.name}.',
                 description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                embed.add_field(name = f'If you need someones attention: ', value = f"Ping {role.mention}, they would be happy to help.")
                await message.channel.send(embed = embed)
                cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                await message.author.add_roles(cool)
                await message.channel.edit(category = cata, sync_permissions = True)
                self.bot.hp2 = True
                await asyncio.sleep(900)
                await message.author.remove_roles(cool)
                await message.channel.edit(category = back)
                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                description = 'If you still have problems, just claim another help channel.', color = discord.Colour.from_rgb(255,221,170))
                await message.channel.send(embed = embed2)
                self.bot.hp2 = False
                
        elif message.channel.id == 754711103665078273 and message.author.id != 7755479510387916871:
            if self.bot.hp3 == True:
                pass
            else:
                embed = discord.Embed(title = f'You have just claimed {message.channel.name}.',
                 description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                embed.add_field(name = f'If you need someones attention: ', value = f"Ping {role.mention}, they would be happy to help.")
                await message.channel.send(embed = embed)
                cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                await message.author.add_roles(cool)
                await message.channel.edit(category = cata, sync_permissions = True)
                self.bot.hp3 = True
                await asyncio.sleep(900)
                await message.author.remove_roles(cool)
                await message.channel.edit(category = back)
                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                description = 'If you still have problems, just claim another help channel.', color = discord.Colour.from_rgb(255,221,170))
                await message.channel.send(embed = embed2)
                self.bot.hp3 = False
                
    @commands.command()
    async def close(self,ctx):
        cata = self.bot.get_channel(754710748353265745)
        if ctx.channel.id == 754710893538836480 or ctx.channel.id == 754710998769991680 or ctx.channel.id == 754711103665078273 and ctx.author.id != 7755479510387916871:
            await ctx.channel.edit(category = cata, sync_permissions = True)
            embed = discord.Embed(title = f"This channel is now open for help.",
             description = 'If you still need help, wait 15 minutes and then take another open channel.', color = discord.Colour.from_rgb(255,221,170))
            await ctx.send(embed = embed)
            if ctx.channel.id == 754710893538836480:
                self.bot.hp1 = False
            elif ctx.channel.id == 754710998769991680:
                self.bot.hp2 = False
            elif ctx.channel.id == 754711103665078273:
                self.bot.hp3 = False

def setup(bot):
    bot.add_cog(Help(bot))