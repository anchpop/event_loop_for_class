from random import randint
from asciimatics.screen import Screen
from time import sleep

def game(screen):
  fish_1 = Fish(0, 4, 1)
  fish_2 = Fish(3, 8, 4)

  while True:
    fish_1.update()
    fish_2.update()
    fish_1.render(screen)
    fish_2.render(screen)

    # ===========
    # Bookkeeping
    # ===========
    ev = screen.get_key()
    if ev in (ord('Q'), ord('q')):
        return
    screen.refresh()
    sleep(1)
    screen.clear()


class Fish:
  position_x = 0
  position_y = 0
  speed = 0

  def __init__(self, position_x, position_y, speed):
    self.position_x = position_x
    self.position_y = position_y
    self.speed      = speed

  def update(self):
    self.position_x += self.speed

  def render(self, screen):
    screen.print_at("><>",
                    self.position_x,
                    self.position_y,
                    colour=2,
                    bg=0)


Screen.wrapper(game)