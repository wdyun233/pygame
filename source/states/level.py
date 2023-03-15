import  pygame
from ..components import info


class Level:

    def __init__(self):
        self.finished = False
        self.next = 'main_menu'
        self.state_name = 'level'
        self.info = info.Info(self.state_name)
    def update(self, surface, keys):
        self.draw(surface)

    def draw(self, surface):
        surface.fill((0, 255, 255))
