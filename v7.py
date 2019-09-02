from random import randint
from asciimatics.screen import Screen
from time import sleep

def game(screen):
  entities = [Fish(0, 4, 1), Fish(3, 8, 4), Fish(2, 19, 6)]

  while True:
    newEntities = []
    for entity in entities:
      newEntities.extend(entity.update(entities))
    for entity in entities:
      entity.render(screen)

    entities.extend(newEntities)

    # ===========
    # Bookkeeping
    # ===========
    ev = screen.get_key()
    if ev in (ord('Q'), ord('q')):
        return
    screen.refresh()
    sleep(.5)
    screen.clear()


class Fish:
  position_x = 0
  position_y = 0
  speed = 0

  def __init__(self, position_x, position_y, speed):
    self.position_x = position_x
    self.position_y = position_y
    self.speed      = speed

  def update(self, entities):
    self.position_x += self.speed
    return [Bubble(self.position_x, self.position_y, 3)]

  def render(self, screen):
    screen.print_at("><>",
                    self.position_x,
                    self.position_y,
                    colour=2,
                    bg=0)


class Bubble:
  position_x = 0
  position_y = 0
  speed = 0

  def __init__(self, position_x, position_y, speed):
    self.position_x = position_x
    self.position_y = position_y
    self.speed      = speed

  def update(self, entities):
    self.position_y += -randint(0, self.speed)
    return []

  def render(self, screen):
    screen.print_at("O",
                    self.position_x,
                    self.position_y,
                    colour=4,
                    bg=0)


Screen.wrapper(game)