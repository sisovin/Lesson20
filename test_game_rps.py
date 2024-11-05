import unittest
from game_rps import rps

class TestRPSGame(unittest.TestCase):
    def setUp(self):
        self.decide_winner = rps('TestPlayer', test=True)

    def test_player_wins_with_rock(self):
        result = self.decide_winner(1, 3)
        self.assertEqual(result, "🎉 You win!")

    def test_player_wins_with_paper(self):
        result = self.decide_winner(2, 1)
        self.assertEqual(result, "🎉 You win!")

    def test_player_wins_with_scissors(self):
        result = self.decide_winner(3, 2)
        self.assertEqual(result, "🎉 You win!")

    def test_computer_wins_with_rock(self):
        result = self.decide_winner(3, 1)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_computer_wins_with_paper(self):
        result = self.decide_winner(1, 2)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_computer_wins_with_scissors(self):
        result = self.decide_winner(2, 3)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_tie_game_with_rock(self):
        result = self.decide_winner(1, 1)
        self.assertEqual(result, "😲 Tie game!")

    def test_tie_game_with_paper(self):
        result = self.decide_winner(2, 2)
        self.assertEqual(result, "😲 Tie game!")

    def test_tie_game_with_scissors(self):
        result = self.decide_winner(3, 3)
        self.assertEqual(result, "😲 Tie game!")

if __name__ == "__main__":
    unittest.main()