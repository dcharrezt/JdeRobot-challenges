
# Python Challenge 

* [challenge info](https://wiki.jderobot.org/store/jmplaza/uploads/gsoc/gsoc2020-python_test.pdf)
* [demo video 1](https://youtu.be/in4N7V-_Yhc)
* [demo video 2](https://youtu.be/6DKsnzFz8BI)

## Python requirements

####  python standard libraries and numpy

* json 
* curses
* collections
* numpy

## Running tests

```bash
python3 -m unittest test_game_of_life.py
```

## Running the app

#### Option 1

```bash
python3 mainapp.py
```

## Structure

```bash
├── config.json
├── game_of_life.py
├── mainapp.py
├── README.md
├── test_game_of_life.py

1 directory, 9 files
```

#### Troubleshooting

If appears an error similar to this one
```bash
_curses.error: addwstr() returned ERR
```
Try reducing the width and height in the config file OR maximizing your terminal.
