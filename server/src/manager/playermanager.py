
class PlayerManager:

    player_repository = None

    def __init__(self, player_repo):
        self.player_repository = player_repo

    def get_players_list(self):
        return self.player_repository.get_players()

    def get_player_by_id(self, player_id):
        return self.player_repository.get_player(player_id)

    def create_player(self, player_id, name):
        return self.player_repository.add_player(player_id)

    def update_player(self, player_id):
        return self.player_repository.update_player(player_id)
    
    def remove_player(self, player_id):
        return self.player_repository.remove_player(player_id)

    
    