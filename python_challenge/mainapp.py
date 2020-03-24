import random
import curses
from curses import textpad
import game_of_life as gol

menu = ['0. Block', '1. Beehive', '2. Loaf', '3. Boat','4. Tub',
        '5. Blinker', '6. Toad', '7. Beacon', '8. Pulsar', '9. Glider',
        'a. LWSpaceship', 'b. MWSpaceship', 'c. HWSpaceship']

def print_menu(stdscr):
    stdscr.addstr(1, 3, "To choose an")
    stdscr.addstr(2, 3, "option press")
    stdscr.addstr(3, 3, "its key or")
    stdscr.addstr(4, 3, "q to quit.")
    for idx, item in enumerate(menu):
        x = 6 + idx
        y = 3
        stdscr.addstr(x, y, item)

def start_game(stdscr):
    # initial settings
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # create a game box
    sh, sw = stdscr.getmaxyx()
    box = [[1,20], [sh-3, sw-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    print_menu(stdscr)

    while 1:
        # non-blocking input
        key = stdscr.getch()

        if key == ord('1'):
            break
        elif key == ord('2'):
            break
        elif key == ord('3'):
            break
        elif key == ord('4'):
            break
        elif key == ord('5'):
            break                        
        elif key == ord('9'):
            break
        elif key == ord('q') or key==ord('Q'):
            break


if __name__ == '__main__':

    game = gol.GameOfLife()

    # curses.wrapper(start_game)