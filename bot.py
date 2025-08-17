import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Synchronisation des slash commands
@bot.event
async def on_ready():
    await bot.tree.sync()  # synchronise les slash commands avec Discord
    print(f"✅ Connecté en tant que {bot.user}")

# Commande slash /ping
@bot.tree.command(name="ping", description="Répond Pong ! 🏓")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong ! 🏓")

# Récupère le token depuis la variable d'environnement
TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)
