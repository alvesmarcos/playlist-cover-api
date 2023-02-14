import asyncio
import aiohttp 
from flask import Flask
from flask import request
from flask_ngrok import run_with_ngrok

from get_genres import get_songs_genres
from prompt import generate_prompt
from uploader import upload_image
from cover_generator import get_cover_image

app = Flask(__name__)

APP_VERSION = "v1"
PORT = 5000

run_with_ngrok(app)

@app.route("/")
def home():
    return { "name": "Playlist Cover API @ Moises Hackathon", "version": "1.0.0" }

@app.route(f"/{APP_VERSION}/cover", methods=['POST'])
async def get_cover():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    songs = data.get("songs")
    
    response_url = await handler_get_cover(title, description, songs)

    return { "url": response_url }

async def handler_get_cover(title, description, songs):
    genres = await get_songs_genres(songs)
    prompt = generate_prompt(title, description, genres)
    path = get_cover_image(prompt)
    url = upload_image(path)
    return url

if __name__ == '__main__':
    app.run()