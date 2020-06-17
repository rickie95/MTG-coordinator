""" 
    Model class for an event.
    An event has: 
    - a name (str)
    - at least one manager (Player)
    - a collection of Players
"""

class Event:

    name = None
    manager_list = []

    players_list = None

    def __init__(self, name, managers):
        """ Creates a new event with a name and at least one manager """
        self.name = name
        self.manager_list = managers
        self.players_list = []

    def add_player(self, player_id):
        """ Add the player id to the event """
        if player_id in self.players_list:
            raise ValueError
        
        self.players_list.append(player_id)

    def remove_player(self, player_id):
        """ Removes the id from players' list """
        self.players_list.remove(player_id)

    def player_is_partecipating(self, player_id):
        """ Return true if player is in players' list """
        return id in self.players_list