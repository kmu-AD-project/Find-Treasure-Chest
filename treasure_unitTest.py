import unittest
import game_function as game

class GameFunctionTest(unittest.TestCase):

    def test_finished_true(self):
        self.newgame = game.Game("EASY")
        self.newgame.goal = 0
        finish = self.newgame.finished()
        self.assertEqual(finish, True)

    def test_finished_false(self):
        self.newgame = game.Game("EASY")
        self.newgame.goal = 1
        finish = self.newgame.finished()
        self.assertEqual(finish, False)

    def test_cellIndex(self):
        self.index = game.Game("EASY").cellIndex(52, 93)
        self.assertEqual(self.index, {'x':0, 'y':0})
