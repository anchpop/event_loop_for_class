from random import randint
from asciimatics.screen import Screen
from time import sleep

def game(screen):
  fish_1_position_x = 0
  fish_1_position_y = 4
  fish_1_speed      = 1

  fish_2_position_x = 3
  fish_2_position_y = 8
  fish_2_speed      = 4

  while True:
    fish_1_position_x += fish_1_speed

    screen.print_at("><>",
                    fish_1_position_x,
                    fish_1_position_y,
                    colour=2,
                    bg=0)


    fish_2_position_x += fish_2_speed

    screen.print_at("><>",
                    fish_2_position_x,
                    fish_2_position_y,
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