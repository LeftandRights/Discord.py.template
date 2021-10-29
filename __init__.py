import discord, os
from discord.ext import commands; os.chdir(__import__('sys').path[0])

Bots = commands.Bot(command_prefix = '!'); Bots.remove_command('help')
Initial_Extension: list = ['cogs.' + Filename[:-3] for Filename in os.listdir('./cogs') if Filename.endswith('.py')]; \
    SetupExtension: None = [(Bots.load_extension(Extension), print('[ Cogs ] >> Extension %s loaded.' % Extension[5:])) for Extension in Initial_Extension]

Bots.run('DiscordBotToken')
