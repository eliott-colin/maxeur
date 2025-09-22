# Maxeur

Maxeur est un bot Discord développé en Python permettant de gérer un système de points au sein d’un serveur.  
Il utilise les commandes slash (`/`) pour interagir avec les utilisateurs.

---

## Fonctionnalités

- `/maxeur @membre` → Attribue un point à un utilisateur.
- `/score [@membre]` → Affiche le score d’un utilisateur (ou le sien par défaut).
- `/leaderboard` → Affiche le classement des utilisateurs en fonction de leurs points.
- `/resetleaderboard` → Réinitialise l’ensemble du classement.

---

## Installation

1. Clonez le projet :
   ```bash
   git clone https://github.com/eliott-colin/maxeur.git
   cd maxeur
   ```
   

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Créez un fichier `.env` contenant votre token Discord :
   ```
   TOKEN=your_discord_token_here
   ```

4. Lancez le bot :
   ```bash
   python bot.py
   ```

---

## Utilisation

- Invitez le bot sur votre serveur avec les permissions nécessaires (applications.commands et bot).  
- Utilisez les commandes slash directement dans Discord pour attribuer des points, consulter les scores et afficher le classement.  

---

## Technologies utilisées

- [Python](https://www.python.org/)  
- [discord.py](https://discordpy.readthedocs.io/)  

---

## Auteur

Projet développé par **eliott-colin**.
