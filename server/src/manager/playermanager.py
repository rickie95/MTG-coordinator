
class PlayerManager:

    player_repository = None

    def __init__(self, player_repo):
        self.player_repository = player_repo

    def get_players_list(self):
        return self.player_repository.get_players()
    