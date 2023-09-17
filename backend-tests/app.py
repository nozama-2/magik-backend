import socketio
import websocket
import requests
import json
import sys
from tangram.colours import *
from tangram.lib import *
from time import sleep

game_id = None
user_id = '0'

ip = '190.92.208.177'
port = '8000'
server_http_url = f"http://{ip}:{port}"
server_socket_url = f"ws://{ip}:{port}"
sio = socketio.Client()
sio.connect(server_socket_url, headers={'userid':user_id, 'connectiontype':'APP'})

def init_game():
	# JS Equivalent of this function is triggered when user clicks button
	global game_id
	data = {
		'user_id': user_id
	}

	resp = requests.post(f'{server_http_url}/equations/start_game', data=json.dumps(data))
	resp_data = json.loads(resp.text)
	game_id = resp_data['game_id']

@sio.on('end_game')
def end_game(data):
	print("Game Ended!")
	# App shuts down

if __name__ == '__main__':
	init_game()