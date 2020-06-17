""" 
    Class for event managment, including data managment
"""

class Event:

    database_name = None
    database_address = None

    players_list = None

    def __init__(self):
        """ Estabilish a db connection and initialize his data """
        self.players_list = []

    def add_player(self, id):
        """ Add the id to the players' list """
        if id in self.players_list:
            raise ValueError
        
        self.players_list.append(id)

    def remove_player(self, id):
        """ Removes the id from players' list """
        self.players_list.remove(id)

    def player_is_partecipating(self, id):
        """ Return true if player is in players' list """
        return id in self.players_list