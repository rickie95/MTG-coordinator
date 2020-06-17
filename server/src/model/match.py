from datetime import datetime

class Match:

    id = None
    players = None # List [ (player1, games_won), (player2, games_won)]
    starting_time = None
    ending_time = None
    winner = None


    def __init__(self, id=None):
        if id is not None:
            self.id = id

        self.players = []

    def add_player(self, player_id):
        if len(self.players) > 2:
            return False

        self.players.append( (player_id, 0) )

    def end_game(self, game_winner_id):
        for p in self.players:
            if p[0].id == game_winner_id:
                p[1] += 1
                if p[1] == 2:
                    self.end_match(p)


    def end_match(self, player):
        self.stop_match()
        self.winner = player   

    def get_score(self):
        return self.players

    ###### Timing ######

    def start_match(self):
        self.starting_time = datetime().now()

    def stop_match(self):
        self.ending_time = datetime().now()

    def has_started(self):
        if self.starting_time is None:
            return False
        
        return True

    def has_ended(self):
        if self.ending_time is None:
            return False

        return True

    def is_progressing(self):
        if self.has_started() and not self.has_ended():
            return True

        return False

    def get_time(self):
        if not self.has_started():
            return 0
        if not self.has_ended():
            return datetime().now() - self.starting_time
        
        return self.ending_time
