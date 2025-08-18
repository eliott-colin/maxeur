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

# Command to remove points from a user
@bot.tree.command(name="minceur", description="Retire un point à un utilisateur")
@app_commands.describe(user="Utilisateur à qui retirer un point")
async def minceur(interaction: discord.Interaction, user: discord.Member):
    user_id = str(user.id)
    if user_id in points and points[user_id] > 0:
        points[user_id] -= 1
        with open(POINTS_FILE, "w") as f:
            json.dump(points, f)
        await interaction.response.send_message(f"{user.mention} a maintenant {points[user_id]} point(s) ! ❌")
    else:
        await interaction.response.send_message(f"{user.mention} n'a pas de points à retirer !")

# Command to check points of a user
@bot.tree.command(name="points", description="Vérifie le nombre de points d'un utilisateur")
@app_commands.describe(user="Utilisateur dont vérifier les points")
async def points_command(interaction: discord.Interaction, user: discord.Member):
    user_id = str(user.id)
    user_points = points.get(user_id, 0)
    await interaction.response.send_message(f"{user.mention} a {user_points} point(s).")

#Leaderboard command to show top users
@bot.tree.command(name="leaderboard", description="Affiche le classement des utilisateurs avec le plus de points")
async def leaderboard(interaction: discord.Interaction):
    sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)
    leaderboard_message = "🏆 **Leaderboard des points** 🏆\n\n"
    
    if not sorted_points:
        leaderboard_message += "Aucun utilisateur n'a de points."
    else:
        for i, (user_id, user_points) in enumerate(sorted_points[:10], start=1):
            user = await bot.fetch_user(int(user_id))
            leaderboard_message += f"{i}. {user.mention} - {user_points} point(s)\n"
    
    await interaction.response.send_message(leaderboard_message)

# Commande pour reset le leaderboard (tout le monde peut le faire)
@bot.tree.command(name="resetleaderboard", description="Réinitialise tous les points du leaderboard")
async def reset_leaderboard(interaction: discord.Interaction):
    points.clear()
    with open("points.json", "w") as f:
        json.dump(points, f)
    await interaction.response.send_message("✅ Le leaderboard a été réinitialisé par {0.mention} !".format(interaction.user))

bot.run(os.getenv("TOKEN"))
