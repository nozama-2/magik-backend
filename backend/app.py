from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit
import os
import json
from uuid import uuid4

# Loads environment variables using dotenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from hctools import dds
# Import routes
# import games

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
socketio = SocketIO(app)

def default():
    return 'Success!'

app.add_url_rule('/', view_func = default, methods = ['GET'])

''' BEGIN WEBSOCKET CONNECTIONS AND ROUTES ------------------
'''

connections =  []

@socketio.on('connect')
def handle_connect(data):
    global connections
    user_id = int(request.headers['Userid'])
    connection_type = request.headers['Connectiontype']

    connections.append({
        'sid': request.sid,
        'connection_type': connection_type,
        'user_id': user_id
    })

    print(f'Client Connected, total clients: {len(connections)}')

@socketio.on('disconnect')
def handle_disconnect():
    global connections
    sid = request.sid
    connections = [i for i in connections if i['sid'] != sid]

    print(f'Client Disconnected, total clients: {len(connections)}')

def start_game():
    global connections
    # Send message to first socket
    data = json.loads(request.data)
    user_id = int(data['user_id'])
    connection_obj = [i for i in connections if i['user_id'] == user_id and i['connection_type'] == 'RASPBERRY_PI']
    
    if len(connection_obj) != 1:
        return 'Please connect rpi game server first!', 300

    sid = connection_obj[0]['sid']
    game_id = str(uuid4())

    data = {
        'user_id': user_id,
        'game_id': game_id
    }

    socketio.emit('start_game', json.dumps(data), room=sid)

    return json.dumps(data)

def end_game():
    global connections
    print ("End Game")
    data = json.loads(request.data)
    user_id = int(data['user_id'])
    game_id = data['game_id']

    print("Updating DDS!")
    dds.add_add_game(data)
    print(data)
    
    connection_obj = [i for i in connections if i['user_id'] == user_id and i['connection_type'] == 'APP']

    if len(connection_obj) != 1:
        return 'Parent Application has been disconnected!', 300

    sid = connection_obj[0]['sid']
    socketio.emit('end_game', data, room=sid)

    return 'Ok, Game Ended Successfully'

app.add_url_rule('/equations/start_game', view_func = start_game, methods = ['POST'])
app.add_url_rule('/equations/end_game', view_func = end_game, methods = ['POST'])

''' END WEBSOCKET CONNECTIONS AND ROUTES ------------------
'''

''' BEGIN GAMES ROUTES ---------------------------
'''

from routes import tangram

app.add_url_rule('/tangram/get_puzzle_image', view_func=tangram.getTangramImage, methods=['POST'])

''' END GAMES ROUTES --------------------------
'''

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=8000)
