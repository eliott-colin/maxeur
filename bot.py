import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=None, intents=intents) 

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Connecté en tant que {bot.user}")

@bot.tree.command(name="ping", description="Répond Pong ! 🏓")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong ! 🏓")

bot.run(os.getenv("TOKEN"))
