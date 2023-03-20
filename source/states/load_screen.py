import  pygame
from ..components import info
from .. import tools, setup, constants as C


class LoadScreen:
    def __init__(self):
        self.finished = False
        self.state_name = 'load_screen'
        self.next = 'level'
        self.info = info.Info(self.state_name)
        self.timer = 0
        self.setup_player()

    def update(self, keys):
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.timer > 2000:
            self.finished = True
            self.timer = 0
        self.info.update(keys)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(self.player, (300, 265))
        self.info.draw(surface)

    def setup_player(self):
        self.player = tools.get_image(setup.GRAPHICS['mario_bros'], 178, 32, 12, 16, (0, 0, 0), C.PLAYER_MULTI)
