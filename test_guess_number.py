import unittest
from guess_number import guess_number

class TestGuessNumberGame(unittest.TestCase):
    def setUp(self):
        self.decide_winner = guess_number('TestPlayer', test=True)

    def test_player_wins(self):
        result = self.decide_winner(1, 1)
        self.assertEqual(result, "🎉 TestPlayer, You won!")

    def test_player_loses(self):
        result = self.decide_winner(1, 2)
        self.assertEqual(result, "Sorry, TestPlayer, You lost! 😢. Better luck next time.")
        
if __name__ == "__main__":
    unittest.main()
