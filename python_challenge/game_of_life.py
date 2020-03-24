import numpy as np
import json

class GameOfLife(object):
    """
    A class used to represent the Game of Life
    """

    def __init__(self):
        """
        Parameters
        ----------
        width : int
            Width of the board, 50 by default.
        height : int
            Height of the board, 50 by default.
        patterns : json, optional
            A json of 2d arrays to certain patterns.
        """

        with open('config.json') as config_file:
            data = json.load(config_file)

        self.width = data['width']
        self.height = data['height']
        self.patterns = data['patterns']

