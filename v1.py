from random import randint
from asciimatics.screen import Screen
from time import sleep

def game(screen):
  while True:

    # ur code go here

    # ===========
    # Bookkeeping
    # ===========
    ev = screen.get_key()
    if ev in (ord('Q'), ord('q')):
        return
    screen.refresh()
    sleep(.5)
    screen.clear()


Screen.wrapper(game)