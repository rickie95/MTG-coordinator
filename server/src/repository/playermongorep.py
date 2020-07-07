class PlayerMongoRepository:
    
    database_address = "localhost"

    def __init__(self):
        self.client = "Opens a connection with mongo"
    
    def get_players(self):
        return ['jon', 'mickey', 'brad']

    def get_player(self, player_id):
        return ['jon']

    def add_player(self, player):
        pass

    def remove_player(self, player):
        pass

    def update_player(self, player):
        pass