import discord
from discord.ext import commands
from discord.ext.commands import Context

class Command(commands.Cog):
    def __init__(self, Bot) -> None: self.Bot = Bot

    @commands.Command()
    async def Hello(self, ctx: Context) -> None:
        await ctx.send('Hi!')

setup = lambda Bot: Bot.add_cog(Command(Bot))