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
sio.connect(server_socket_url, headers={'userid':user_id, 'connectiontype':'RASPBERRY_PI'})

@sio.on('start_game')
def init_game(data):
	global game_id
	print("Initialised Game!")

	data = json.loads(data)
	game_id = data['game_id']
	print(f"Game Id: {game_id}")

	# Play the game

def end_game():
	# Call this function when u done playing game
	sample_data = {
		'user_id': user_id,
		'game_id': game_id,
		'sovle_time': '00:00:10',
		'solve_state': 'success',
		'session_duration': 34
	}

	print(sample_data)
	resp = requests.post(f'{server_http_url}/equations/end_game', data=json.dumps(sample_data))
	print(resp.text)

# Basically whatever is thrown into end game is thrown into DDS
# So pls be nice to it lol

runs = 0
while True:
	runs += 1
	print("Reloaded!")

	# Run pygame stuff here

	sleep(1.0)

	if runs > 10:
		# End game
		end_game()
		sys.exit(0)