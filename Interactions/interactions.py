#Interactions cog for PeashyCogs
#I know there are better ways of doing this but
#This way works fine for what it is used for
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
        embed.add_field(name="interactions", value="**hug** - Give someone a nice warm hug\n**headpats** - give someone some nice headpats\n**high5** - Give someone a right nice high five!\n**slap** - Be a bully and slap someone\n**kiss** - give someone a kiss\n**wag** - Wag your fluffy tail", inline=True)
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

        imgs = ['https://i.imgur.com/SEXXYQQ.gif','https://i.imgur.com/e2paJmu.gif','https://i.imgur.com/tbJux74.gif','https://i.imgur.com/JNM6LDM.gif',
                'https://i.imgur.com/SJwUxts.gif','https://i.imgur.com/EPp6a1N.gif','https://i.imgur.com/QalbZl8.gif','https://i.imgur.com/w8ompSg.gif',
                'https://i.imgur.com/3QxbvCg.gif','https://i.imgur.com/70uuH0f.gif','https://i.imgur.com/EJneSBP.gif','https://i.imgur.com/mNqI3VW.gif',
                'https://i.imgur.com/srPDfQk.gif','https://i.imgur.com/wDTQP63.gif','https://i.imgur.com/V8kBDkb.gif','https://i.imgur.com/sfKRPJA.gif',
                'https://i.imgur.com/K3oPzyf.gif','https://i.imgur.com/hmgJm9s.gif']

        if author.id == user.id:
            return await self.bot.say("You can't hug yourself! Silly!")
        else:
            embed=discord.Embed(title="Hugs! <3", color=0xe8cdff)
            embed.set_image(url='{}'.format(random.choice(imgs)))
            await self.bot.say("{} you got a hug from {}!".format(user.mention, author.mention), embed=embed)


    @commands.command(pass_context=True, no_pm=True)
    async def slap(self, ctx, user: discord.Member):
        
        author = ctx.message.author
        """Slap someone like the bully you are"""

        imgs = ['https://i.imgur.com/4Dmr3VL.gif','https://i.imgur.com/oHIhx7M.gif','https://i.imgur.com/jQ2husB.gif','https://i.imgur.com/3peMaBW.gif',
                'https://i.imgur.com/RUbi6d0.gif','https://i.imgur.com/tl00674.gif','https://i.imgur.com/bcrq8ub.gif','https://i.imgur.com/eaTWpXY.gif',
                'https://i.imgur.com/Glv9li5.gif','https://i.imgur.com/dYTciGM.gif','https://i.imgur.com/yM6D8cP.gif','https://i.imgur.com/1AV8qoP.gif',
                'https://i.imgur.com/Wl9afKr.gif','https://i.imgur.com/USqA7xv.gif','https://i.imgur.com/AwNzgAM.gif']

        if author.id == user.id:
            return await self.bot.say("No bully yourself!")
        else:
            embed=discord.Embed(title="Ouch!", color=0xe8cdff)
            embed.set_image(url='{}'.format(random.choice(imgs)))
            await self.bot.say("{} You got slapped by bully {}!".format(user.mention, author.mention), embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def kiss(self, ctx, user: discord.Member):
        
        author = ctx.message.author
        """Give someone a right nice kiss"""

        imgs = ['https://i.imgur.com/5hMtWO9.gif','https://i.imgur.com/HKsSl9p.gif','https://i.imgur.com/eb9t4tC.gif','https://i.imgur.com/xfeBp2I.gif',
                'https://i.imgur.com/sFVZDDx.gif','https://i.imgur.com/xfeBp2I.gif','https://i.imgur.com/sFVZDDx.gif','https://i.imgur.com/6Rp0p9R.gif',
                'https://i.imgur.com/1MaQASb.gif','https://i.imgur.com/fe5HEvG.gif','https://i.imgur.com/YE5FsnO.gif','https://i.imgur.com/jdFAUlR.gif',
                'https://i.imgur.com/HnfejJb.gif','https://i.imgur.com/j05lIrM.gif','https://i.imgur.com/c3yMq5E.gif','https://i.imgur.com/tIrNb1L.gif']

        if author.id == user.id:
            return await self.bot.say("You can't kiss yourself silly!")
        else:
            embed=discord.Embed(title="Smooch!", color=0xe8cdff)
            embed.set_image(url='{}'.format(random.choice(imgs)))
            await self.bot.say("{} You got a kiss from {}!!".format(user.mention, author.mention), embed=embed)
    
    @commands.command(pass_context=True, no_pm=True)
    async def wag(self, ctx):
        
        author = ctx.message.author
        """Wag your fluffy tail!"""

        imgs = ['https://i.imgur.com/3fV9SG5.gif','https://i.imgur.com/9Geusxk.gif','https://i.imgur.com/aX828Eg.gif','https://i.imgur.com/8YTruSY.gif',
                'https://i.imgur.com/Gu3ifdb.gif','https://i.imgur.com/x1f8pxf.gif','https://i.imgur.com/fv7nrT9.gif','https://i.imgur.com/yHqegf3.gif',
                'https://i.imgur.com/y5SVgJ6.gif','https://i.imgur.com/4IuUR6D.gif','https://i.imgur.com/VaSM5ST.gif','https://i.imgur.com/F0m8reG.gif',
                'https://i.imgur.com/9H7vC6t.gif','https://i.imgur.com/uXOQtNI.gif']
                
        embed=discord.Embed(title="wag wag", color=0xe8cdff)
        embed.set_image(url='{}'.format(random.choice(imgs)))
        await self.bot.say("{} wags their tail!".format(author.mention), embed=embed)

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
