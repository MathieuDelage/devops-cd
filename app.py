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

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)