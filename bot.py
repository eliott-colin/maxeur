import discord
from discord.ext import commands
from discord import app_commands
import os
import json


# Load points from a JSON file
POINTS_FILE = "points.json"
if os.path.exists(POINTS_FILE):
    with open(POINTS_FILE, "r") as f:
        points = json.load(f)
else:
    points = {}

# bot configuration
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=None, intents=intents) 

# bot event
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Connecté en tant que {bot.user}")

# Command to add points to a user
@bot.tree.command(name="maxeur", description="Ajoute un point à un utilisateur")
@app_commands.describe(user="Utilisateur à qui ajouter un point")
async def maxeur(interaction: discord.Interaction, user: discord.Member):
    user_id = str(user.id)
    points[user_id] = points.get(user_id, 0) + 1
    with open(POINTS_FILE, "w") as f:
        json.dump(points, f)
    await interaction.response.send_message(f"{user.mention} a maintenant {points[user_id]} point(s) ! ✅")


bot.run(os.getenv("TOKEN"))
