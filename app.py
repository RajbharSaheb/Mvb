from flask import Flask, jsonify, render_template
from pyrogram import Client
import asyncio
import os

app = Flask(__name__)

api_id = int(os.environ.get("API_ID", "YOUR_API_ID"))
api_hash = os.environ.get("API_HASH", "YOUR_API_HASH")
bot_token = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
channel_username = os.environ.get("CHANNEL_USERNAME", "YOUR_CHANNEL_USERNAME_OR_ID")

# Create bot client globally
bot = Client(
    "bot_session",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# Start the bot client only once
loop = asyncio.get_event_loop()
loop.run_until_complete(bot.start())

async def fetch_movies():
    movies = []
    async for message in bot.get_chat_history(channel_username, limit=50):
        if message.document or message.video:
            title = message.caption if message.caption else "No title"
            file_size = message.document.file_size if message.document else message.video.file_size
            link = f"https://t.me/{channel_username.lstrip('@').lstrip('-100')}/{message.message_id}"
            movies.append({
                "title": title,
                "file_size": round(file_size / (1024 * 1024), 2),  # MB
                "link": link
            })
    return movies

@app.route("/api/movies")
def api_movies():
    movies = loop.run_until_complete(fetch_movies())
    return jsonify(movies)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
