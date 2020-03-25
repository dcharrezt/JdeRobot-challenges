import numpy as np
import json
import curses
from collections import OrderedDict 
from curses import textpad
import time

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
        self.menu = OrderedDict([(ord('0'), 'Block'), (ord('1'), 'Beehive'), (ord('2'), 'Loaf'), 
                        (ord('3'), 'Boat'), (ord('4'), 'Tub'),(ord('5'), 'Blinker'), 
                        (ord('6'), 'Toad'), (ord('7'), 'Beacon'), (ord('8'), 'Pulsar'),
                        (ord('9'), 'Pentadecathlon'), (ord('a'), 'Glider'), (ord('b'), 'LWSpaceship'), 
                        (ord('c'), 'MWSpaceship'), (ord('d'), 'HWSpaceship')])
        self.board = np.zeros((self.height, self.width))

    def get_neighbours(self, x, y):
        neighbours = []
        for x2 in range(x-1, x+2):
            for y2 in range(y-1, y+2):
                if ((-1<x < self.height) and (-1<y < self.width) and
                    (x != x2 or y != y2) and (0 <= x2 < self.height) and 
                                                (0 <= y2 < self.width)):
                    neighbours.append([x2,y2])
        return  neighbours

    def update_game(self):
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
        curses.wrapper(self.menu_controller)    

    def print_menu(self, stdscr):
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

    def draw_pattern(self, stdscr):
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == 1:
                    stdscr.addstr(y+2, x+21, '*')
                else:
                    stdscr.addstr(y+2, x+21, ' ')         

    def menu_controller(self, stdscr):
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
                for i in range(len(self.patterns[self.menu[key]])):
                    for j in range(len(self.patterns[self.menu[key]][0])):
                        self.board[i+10][j+10] = self.patterns[self.menu[key]][i][j]
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                self.draw_pattern(stdscr)
                self.update_game()
                    
            elif key == ord('q') or key==ord('Q'):
                break