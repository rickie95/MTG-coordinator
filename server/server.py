from flask import Flask
from flask import jsonify, Response, render_template
from markupsafe import escape
from flask_socketio import SocketIO, send, emit

from src.manager.playermanager import PlayerManager
from src.repository.playermongorep import PlayerMongoRepository

player_repo = PlayerMongoRepository()
player_manager = PlayerManager(player_repo)

app = Flask(__name__)
socketio = SocketIO(app, logger=True, always_connect=True)
 
@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/players')
def get_players_list():
    players = player_manager.get_players_list()
    return jsonify([p for p in players])

@app.route('/players/<player_id>', methods=['GET', 'DELETE'])
def player_by_id(player_id):
    result = None

    if request.method == 'GET':
        result = player_manager.get_player_by_id(player_id)

    if request.method == 'DELETE':
        result = player_manager.remove_player(player_id)

    if result is None:
        return Response(" { 'player' : 'unknown' }", status=404, mimetype='application/json')

    return jsonify(result)

@app.route('/players/<player_id>',  methods=['POST', 'PUT'])
def player_(player_id):
    result = None

    if request.method == 'POST':
        name = request.args.get('name')
        result = player_manager.create_player(player_id, name)

    if request.method == 'PUT':
        result = player_manager.update_player(player_id)

    # If everething is gone ok, then answer a 200
    if result is True:
        return Response(" { 'player' : 'found' }", status=200, mimetype='application/json')
    
    return Response(" { 'player' : 'unknown' }", status=404, mimetype='application/json')


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

@socketio.on('connect')
def handle_connection():
    print("A client has connected")

@socketio.on('message')
def handle_message(message):
    print(message)
    send('okmesg')


@socketio.on('fromApp')
def handle_message(message):
    print('fromApp: ' + message)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
