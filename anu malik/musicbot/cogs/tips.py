from discord.ext import commands
import discord
import random


class Tips(commands.Cog):
    """Commands for providing tips about using the bot."""

    def __init__(self, bot, config):
        self.bot = bot
        self.config = config[__name__.split(".")[-1]]
        self.tips = ["Only admins and the song requester can immediately skip songs. Everybody else will have to vote!",
                     f"Ye video dekh be aur kitne tips chahiye?: {self.config['github_url']}", "chup be nalayak zyada aukat aa rhi hai kya?", "sex kardunga pata bhi nahi chalega", "https://media.discordapp.net/attachments/830551169487077446/887345973020471306/20210914_075523.jpg?width=657&height=430"]

    @commands.command()
    async def tip(self, ctx):
        """Get a random tip about using the bot."""
        index = random.randrange(len(self.tips))
        await ctx.send(f"**Tip #{index+1}:** {self.tips[index]}")
