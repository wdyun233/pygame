import  pygame
from ..components import info


class LoadScreen:
    def __init__(self):
        self.finished = False
        self.state_name = 'load_screen'
        self.next = 'level'
        self.info = info.Info(self.state_name)
        self.timer = 0


    def update(self, surface, keys):
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.timer > 2000:
            self.finished = True
            self.timer = 0
        self.draw(surface)
        self.info.update()
        self.info.draw(surface)
    def draw(self, surface):
        surface.fill((0, 0, 0))
