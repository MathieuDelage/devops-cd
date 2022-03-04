"""
Projet de démo pour la création d'un CD
"""
from flask import Flask
import os

# Récupération des ENVs
PORT = os.environ.get("PORT", 80)
HOST = os.environ.get("HOST", "0.0.0.0")

app = Flask("demo")

@app.get("/")
def hello():
    """Fonction appellée pour le chemin par défaut.

    Returns:
        str: un message de la plus grande importance
    """
    return "Hello, World !"

@app.get('/poulet')
def poulet():
    """Fonction appellée pour le chemin /poulet.

    Returns:
        str: un message de la plus grande importance
    """
    return "Hello Poulet !"

@app.get('/lapin')
def poulet():
    """Fonction appellée pour le chemin /lapin.

    Returns:
        str: un message de la plus grande importance
    """
    return "Hello Lapin !"

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)