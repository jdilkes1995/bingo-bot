from discord.ext import commands

class create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Example command
    @commands.command()
    async def create(self, ctx, ): 
        await ctx.send("Bingo!")

async def setup(bot):
    await bot.add_cog(create(bot))