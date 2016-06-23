from flask import Flask, render_template, request, jsonify
import datetime, json, time, requests, eventlet
import array, fcntl, time, signal, sys, random, re
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin

eventlet.monkey_patch()

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!'
# app.config['DEBUG'] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

socketio = SocketIO(app, async_mode='eventlet')

# Get system information
# Get available podcasts
# Play podcast
# Update play status

clients = 0

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/auth", methods=['GET'])
@cross_origin()
def auth():
    print('Auth attempt')
    return jsonify(status=200, id="rpicar")

@socketio.on('connect', namespace='/socket')
def connect():
    # Return status of system, register client.
    global clients
    id = random.getrandbits(128)
    clients += 1
    socketio.emit('session', id, namespace='/socket')
    socketio.emit('message', {'status': 'ok', 'message': {'uptime': 34324352, 'health': 'good'}}, namespace='/socket')
    socketio.emit('message', {'status': 'ok', 'message': clients}, namespace='/socket')

@socketio.on('message', namespace='/socket')
def message(message):
    socketio.emit('message', {'status': 'default', 'message':  message['text'], 'client': message['id']}, namespace='/socket')

@socketio.on('disconnect', namespace='/socket')
def disconnect():
    global clients
    clients -= 1
    socketio.emit('message', {'status': 'error', 'message': 'User disconnected'}, namespace='/socket')

@socketio.on('status', namespace='/socket')
def status_update():
    # Send message to all clients
    socketio.emit('message', {'status': 'default', 'message': 'Status should be object'}, namespace='/socket')


if __name__ == "__main__":
  socketio.run(app, host="0.0.0.0")
