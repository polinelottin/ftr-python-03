from flask import Flask, jsonify, request, send_file, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=["GET"])
def chat():
    print("Chat")
    return render_template("index.html")

#websockets
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(input):
    print(input)
    socketio.emit('message', input)

if __name__ == "__main__":
    socketio.run(app, port=5000, debug=True)