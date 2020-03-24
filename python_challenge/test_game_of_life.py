import unittest
import game_of_life as gol

class TestGameOfLife(unittest.TestCase):
    """
    Test the add GameOfLife class
    """
    def setUp(self):
        self.game = gol.GameOfLife()

    def test_default_board_dimensions(self):
        """
        Test that the dimensions are loaded properly from the config.json
        """

        self.assertEqual(self.game.width, 50)
        self.assertEqual(self.game.height, 50)


if __name__ == '__main__':
    unittest.main()