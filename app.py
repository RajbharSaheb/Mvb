from flask import Flask, jsonify, render_template
from pyrogram import Client
import os

api_id = int(os.environ.get("API_ID", "YOUR_API_ID")
api_hash = os.environ.get("API_HASH", "YOUR_API_HASH")
channel_id = os.environ.get("CHANNEL_ID", "YOUR_CHANNEL_ID")

app = Flask(__name__)

bot = Client("movie_site_bot", api_id=api_id, api_hash=api_hash)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/movies")
def get_movies():
    movies = []
    with bot:
        for message in bot.get_chat_history(channel_id, limit=30):
            if message.video or message.document:
                title = message.caption if message.caption else "No Title"
                link = f"https://t.me/{channel_id}/{message.message_id}"

                thumb = "https://via.placeholder.com/300x450.png?text=No+Image"
                if message.video and message.video.thumbs:
                    # thumb logic skip, placeholder use
                    pass

                movies.append({
                    "title": title,
                    "link": link,
                    "thumb": thumb
                })
    return jsonify(movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
