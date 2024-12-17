import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user} (ID: {bot.user.id})")
    print("---------------------------")

@bot.command
async def hello(ctx):
    await ctx.send(f'Hi! I\'m {bot.user}!')

@bot.command()
async def mem(ctx):
    with open('file/MEME.jpg', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)

