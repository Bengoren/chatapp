from flask import Flask, send_file, request, jsonify
from datetime import datetime
import mysql.connector
import os

# Implemented by Ben
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Implemented by Ben
def get_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

app = Flask(__name__)

# Implemented by Liron
@app.route('/')
def index():
    return send_file('index.html')

# Implemented by Liron
@app.get("/<room>")
def serve_room(room):
    return send_file("index.html")

# Implemented by Ben
@app.route('/api/chat/<room>')
def get_chat(room):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT username, message, created_at
            FROM messages
            WHERE room = %s
            ORDER BY created_at ASC
        """
        cursor.execute(query, (room,))
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        output = ""
        for row in rows:
            output += f"[{row['created_at']}] {row['username']}: {row['message']}\n"

        return output

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Implemented by Liron
@app.post('/api/chat/<room>')
def post_chat(room):
    try:
        username = request.form.get("username")
        message = request.form.get("msg")

        if not username or not message:
            return jsonify({"error": "username and message required"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO messages (room, username, message, created_at)
            VALUES (%s, %s, %s, NOW())
        """
        cursor.execute(query, (room, username, message))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
