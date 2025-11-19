from flask import Flask, send_file, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Ensure chats directory exists
if not os.path.exists("chats"):
    os.makedirs("chats")

# Serve index.html for root
@app.route('/')
def index():
    return send_file('index.html')

# Serve index.html for any room
@app.get("/<room>")
def serve_room(room):
    return send_file("index.html")

# GET chat messages (returns raw text for your JS)
@app.route('/api/chat/<room>')
def get_chat(room):
    chat_file = f'chats/{room}'
    if not os.path.exists(chat_file):
        return ""  # return empty string if no messages yet
    with open(chat_file, "r", encoding="utf-8") as f:
        return f.read()

# POST chat messages (reads 'username' and 'msg' from your form)
@app.post('/api/chat/<room>')
def post_chat(room):
    username = request.form.get("username")
    message = request.form.get("msg")  # matches your input name

    if not username or not message:
        return jsonify({"error": "username and message required"}), 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat_entry = f"[{timestamp}] {username}: {message}\n"

    chat_file = f'chats/{room}'
    with open(chat_file, "a", encoding="utf-8") as f:
        f.write(chat_entry)

    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

