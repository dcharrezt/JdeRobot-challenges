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

        self.assertEqual(self.game.width, 90)
        self.assertEqual(self.game.height, 45)

    def test_get_neighbours(self):
        """
        Test the function get neighbours returns correctly the list of neighbours
        """
        self.assertEqual(self.game.get_neighbours(2,2), [[1, 1], [1, 2], [1, 3], 
                                        [2, 1], [2, 3], [3, 1], [3, 2], [3, 3]])
        self.assertEqual(self.game.get_neighbours(0,0), [[0, 1], [1, 0], [1, 1]])
        self.assertEqual(self.game.get_neighbours(44,0), [[43, 0], [43, 1], [44, 1]])
        self.assertEqual(self.game.get_neighbours(45,0), [])
        self.assertEqual(self.game.get_neighbours(44,89), [[43, 88], [43, 89], [44, 88]])


    def test_update_game(self):
        """
        Testing the function that updates the board, it should abide the rules of
        game of life.
        """ 
        for i in range(3):
            for j in range(3):
                self.game.board[i][j] = self.game.patterns["Blinker"][i][j]
        self.game.update_game()
        self.assertEqual(self.game.board[0][1], 1)
        self.assertEqual(self.game.board[1][1], 1)
        self.assertEqual(self.game.board[2][1], 1)
            
    def test_key_pressed(self):
        self.assertEqual(self.game.patterns[self.game.menu[ord('9')]], [[1, 1, 1], [1, 0, 1], 
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]])
    

if __name__ == '__main__':
    unittest.main()