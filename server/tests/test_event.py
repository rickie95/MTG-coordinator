from unittest.mock import MagicMock
import unittest

from src.model.event import Event
from src.model.player import Player

PLAYER_ID = "Fooo_123"
EVENT_NAME = "FooEvent"
MANAGERS_LIST = [Player("Foo"), Player("Bar")]

class EventTest(unittest.TestCase):

    def setUp(self):
        self.event = Event(EVENT_NAME, MANAGERS_LIST)

    def test_initial_status(self):
        """ Player list must be empty """
        self.assertFalse(self.event.players_list)

    def test_add_player(self):
        """ add_player should add the id to the players' list """
        self.event.add_player(PLAYER_ID)

        self.assertTrue(PLAYER_ID in self.event.players_list)

    def test_add_player_already_present(self):
        """ Adding again a player should trows a ValueError """
        self.event.add_player(PLAYER_ID)
        self.assertRaises(ValueError, self.event.add_player, PLAYER_ID)

    def test_remove_player(self):
        """ remove_player should remove player's id if present """
        self.event.add_player(PLAYER_ID)
        self.assertTrue(PLAYER_ID in self.event.players_list)

        self.event.remove_player(PLAYER_ID)
        self.assertFalse(PLAYER_ID in self.event.players_list)

    def test_remove_non_existent_player(self):
        """ Removing a non existent id should trows a ValueError """
        self.assertRaises(ValueError, self.event.remove_player, PLAYER_ID)

if __name__ == '__main__':
    unittest.main(buffer=False)