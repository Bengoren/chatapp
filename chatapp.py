from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')



@app.get("/<room>")
def serve_room(room):
    return send_file("index.html")


@app.route('/api/chat/<room>')
def get_chat(room):
    # Path to the chat file for this room
    chat_file = f'chats/{room}.txt'



if __name__ == '__main__':
    app.run(debug=True)


