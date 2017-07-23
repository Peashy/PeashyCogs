#Headpats cog by Danneh(peashy/neptunia)
import discord
from discord.ext import commands
import random


class Interactions:
    """Fun little social interactions"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def interactions(self, ctx):
        """Gives a list of interactions and a bit of help"""

        embed=discord.Embed(title="Interactions help", description="Here is a list of interactions you can use", color=0xb9ffe5)
        embed.add_field(name="interactions", value="**hug** - Give someone a nice warm hug\n**headpats** - give someone some nice headpats\n**high5** - Give someone a right nice high five!", inline=True)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def headpat(self, ctx, user: discord.Member):
        
        author = ctx.message.author
        """Give headpats to someone!"""

        imgs = ['https://i.imgur.com/36HgI7H.gif','https://i.imgur.com/6wVW3lH.gif','https://i.imgur.com/D1yHQD2.gif','https://i.imgur.com/SqHw3OG.gif',
                'https://i.imgur.com/9prO8ZK.gif','https://i.imgur.com/Sweq7sK.gif','https://i.imgur.com/H7diTRA.gif','https://i.imgur.com/GMSHYle.gif',
                'https://i.imgur.com/lYcEVzv.gif','https://i.imgur.com/V0cweWP.gif','https://i.imgur.com/BCIzgVn.gif','https://i.imgur.com/TZT9zzQ.gif',
                'https://i.imgur.com/5rbEz4O.gif','https://i.imgur.com/JYbEjFN.gif','https://i.imgur.com/PyNlOqq.gif','https://i.imgur.com/rOO2bNR.gif',
                'https://i.imgur.com/j8ZnAgL.gif','https://i.imgur.com/ZHE8acK.gif']

        if author.id == user.id:
            return await self.bot.say("You can't headpat yourself!")
        else:
            embed=discord.Embed(title="Headpats! <3", color=0xf2b5e3)
            embed.set_image(url='{}'.format(random.choice(imgs)))
            await self.bot.say("{} you got headpats from {}!".format(user.mention, author.mention), embed=embed)


    @commands.command(pass_context=True, no_pm=True)
    async def hug(self, ctx, user: discord.Member):
        
        author = ctx.message.author
        """Give someone a nice comfy hug"""

        imgs = ['https://i.imgur.com/70uuH0f.gif','https://i.imgur.com/EJneSBP.gif','https://i.imgur.com/mNqI3VW.gif','https://i.imgur.com/srPDfQk.gif',
                'https://i.imgur.com/wDTQP63.gif','https://i.imgur.com/V8kBDkb.gif','https://i.imgur.com/sfKRPJA.gif','https://i.imgur.com/No8oJ9p.gif',
                'https://i.imgur.com/K3oPzyf.gif','https://i.imgur.com/hmgJm9s.gif','https://i.imgur.com/3QxbvCg.gif','https://i.imgur.com/w8ompSg.gif',
                'https://i.imgur.com/JNM6LDM.gif','https://i.imgur.com/EPp6a1N.gif','https://i.imgur.com/QalbZl8.gif','https://i.imgur.com/tbJux74.gif']

        if author.id == user.id:
            return await self.bot.say("You can't hug yourself! Silly!")
        else:
            embed=discord.Embed(title="Hugs! <3", color=0xe8cdff)
            embed.set_image(url='{}'.format(random.choice(imgs)))
            await self.bot.say("{} you got a hug from {}!".format(user.mention, author.mention), embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def high5(self, ctx, user: discord.Member):
        
        author = ctx.message.author
        """Give someone a right nice high five!"""

        if author.id == user.id:
            return await self.bot.say("Self highfive hell yeah!")
        else:
            await self.bot.say("{} Highfive from {}! :hand_splayed: ".format(user.mention, author.mention))


def setup(bot):
    bot.add_cog(Interactions(bot))