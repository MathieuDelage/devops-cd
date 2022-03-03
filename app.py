from flask import Flask
import os

PORT = os.environ.get("PORT", 80)
HOST = os.environ.get("HOST", "0.0.0.0")

app = Flask("demo")

@app.get("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)