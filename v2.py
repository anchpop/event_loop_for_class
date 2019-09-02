from random import randint
from asciimatics.screen import Screen
from time import sleep

def game(screen):
  fish_position_x = 0
  fish_position_y = 4
  fish_speed      = 1

  while True:
    fish_position_x += fish_speed

    screen.print_at("><>",
                    fish_position_x,
                    fish_position_y,
                    colour=2,
                    bg=0)


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