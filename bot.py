import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

# Exemple de commande simple
@bot.command()
async def ping(ctx):
    await ctx.send("Pong ! 🏓")

# Récupère le token depuis la variable d'environnement
TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)