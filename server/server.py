from flask import Flask
from flask import jsonify
from markupsafe import escape

from src.manager.playermanager import PlayerManager
from src.repository.playermongorep import PlayerMongoRepository

player_repo = PlayerMongoRepository()
player_manager = PlayerManager(player_repo)

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/players')
def get_players_list():
    players = player_manager.get_players_list()
    return jsonify([p for p in players])

@app.route('/players/<player_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def player_by_id(player_id):
    if request.method == 'GET':
        pass # get player info
    if request.method == 'POST':
        pass # set new player
    if request.method == 'DELETE':
        pass # delete player
    if request.method == 'PUT':
        pass # update player info

    return 'ok'

@app.route('/event/<player_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def player_joins_event(player_id):
    if request.method == 'GET':
        pass # get event info about the player
    if request.method == 'POST':
        pass # player joins event
    if request.method == 'DELETE':
        pass # remove player from event
    if request.method == 'PUT':
        pass # update player info about event
    
    return 'ok'

@app.route('/matches', methods=['GET'])
def get_results():
    ''' Returns a JSON with all matches' status'''
    return 'all good'

@app.route('/matches/<match_id>/<player_id>/<action>')
def player_action(match_id, player_id, action):
    print("match: {}\nplayer: {}\n{}.".format(escape(match_id), escape(player_id), escape(action)))
    return 'ok'

