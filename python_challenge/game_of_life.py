import numpy as np
import json # python standard library 
import curses # python standard library 
import time # python standard library 
from collections import OrderedDict # python standard library  
from curses import textpad # python standard library 


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
        patterns : json
            A json of 2d arrays of initialize the game of life.
        menu : OrderecdDict
            An ordered dict mapping keys and id of the pattern
        board : 2d array
            numpy matrix that represents the board, initialized with zeros
        """
        
        with open('config.json') as config_file:
            data = json.load(config_file)

        self.width = data['width']
        self.height = data['height']
        self.patterns = data['patterns']
        self.menu = OrderedDict([(ord('0'), 'Block'), (ord('1'), 'Beehive'), (ord('2'), 'Loaf'), 
                        (ord('3'), 'Boat'), (ord('4'), 'Tub'),(ord('5'), 'Blinker'), 
                        (ord('6'), 'Toad'), (ord('7'), 'Beacon'), (ord('8'), 'Pulsar'),
                        (ord('9'), 'Pentadecathlon'), (ord('a'), 'Glider'), (ord('b'), 'LWSpaceship'), 
                        (ord('c'), 'MWSpaceship'), (ord('d'), 'HWSpaceship'), (ord('e'), 'Random')])
        self.board = np.zeros((self.height, self.width))

    def get_neighbours(self, x, y):
        """
        Given a cell position returns a lists of the cell's neighbours positions

        Parameters
        ----------
        x : int
            X coordinate of the cell that which neighbours are going to be retrieved
        y : int
            Y coordinate of the cell that which neighbours are going to be retrieved
        Returns
        ----------
        neighbours: list[]
            Returns the x and y coordinates of the neighbours from the queried positions
        """
        neighbours = []
        for x2 in range(x-1, x+2):
            for y2 in range(y-1, y+2):
                if ((-1<x < self.height) and (-1<y < self.width) and
                    (x != x2 or y != y2) and (0 <= x2 < self.height) and 
                                                (0 <= y2 < self.width)):
                    neighbours.append([x2,y2])
        return  neighbours

    def update_game(self):
        """
        Updates cells to comply the game of life's rules

        Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        Any live cell with two or three live neighbours lives on to the next generation.
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        changes = [] 
        for i in range(self.width):
            for j in range(self.height):
                neighbours = list(self.get_neighbours(j,i))
                n_neighbours = 0
                for cell in neighbours:
                    if self.board[cell[0]][cell[1]] == 1:
                        n_neighbours += 1
                       
                if n_neighbours == 3 and not self.board[j][i]:
                    changes.append([j,i,1])
                elif (n_neighbours < 2 or n_neighbours > 3) and self.board[j][i]:
                    changes.append([j,i,0])
                elif (2 == n_neighbours or n_neighbours == 3) and self.board[j][i]:
                    changes.append([j,i,1])
        for c in changes:
            self.board[c[0]][c[1]] = c[2]


    def start_game(self):
        """
        Initializes the game environment
        """
        curses.wrapper(self.menu_controller)    

    def print_menu(self, stdscr):
        """
        Renders the left menu in the stdscr window

         Parameters
        ----------
        stdscr : Window
            Window object representing the entire screen
        """
        stdscr.addstr(1, 3, "To choose an")
        stdscr.addstr(2, 3, "option press")
        stdscr.addstr(3, 3, "its key or")
        stdscr.addstr(4, 3, "q to quit.")
        for idx, item in enumerate(self.menu):
            x = 6 + idx
            y = 3
            if idx>9:
                stdscr.addstr(x, y, chr(idx+87)+'. '+self.menu[item])
            else:
                stdscr.addstr(x, y, str(idx)+'. '+self.menu[item])
        stdscr.addstr(23, 3, "And press ENTER")
        stdscr.addstr(24, 3, "to show the")
        stdscr.addstr(25, 3, "next step!")
        

    def draw_pattern(self, stdscr):
        """
        Renders the self.board where 0s are updated as empty spaces and
        1s are updated as * in the stdscr window

        Parameters
        ----------
        stdscr : Window
            Window object representing the entire screen
        """
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == 1:
                    stdscr.addstr(y+2, x+21, '*')
                else:
                    stdscr.addstr(y+2, x+21, ' ')         

    def menu_controller(self, stdscr):
        """
        Handles the key up events and calls two helper functions draw_patters and print_menu
        to render into the stdscr window

        Parameters
        ----------
        stdscr : Window
            Window object representing the entire screen
        """

        curses.curs_set(0)
        stdscr.nodelay(1)
        stdscr.timeout(100)

        box_height, box_width = stdscr.getmaxyx()
        box = [[1,20], [box_height-3, box_width-3]]
        textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

        self.draw_pattern(stdscr)
        self.print_menu(stdscr)

        while 1:
            key = stdscr.getch()
            if key in self.menu:
                self.board = np.zeros((self.height, self.width))
                if key == ord('e') or key == ord('E'):
                    self.board = np.random.randint(2, size=(self.height, self.width))
                else:
                    for i in range(len(self.patterns[self.menu[key]])):
                        for j in range(len(self.patterns[self.menu[key]][0])):
                            self.board[i+10][j+10] = self.patterns[self.menu[key]][i][j]
                self.draw_pattern(stdscr)
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                self.update_game()
                self.draw_pattern(stdscr)
                    
            elif key == ord('q') or key==ord('Q'):
                break