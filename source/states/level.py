import  pygame
from ..components import info, player
from .. import setup, constants as C, tools


class Level:

    def __init__(self):
        self.finished = False
        self.next = 'main_menu'
        self.state_name = 'level'
        self.info = info.Info(self.state_name)
        self.setup_background()
        self.setup_player()

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(rect.width*C.BG_MULTI), int(rect.height*C.BG_MULTI)))
        self.background_rect = self.background.get_rect()

    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def update(self, keys):
        self.update_player_position()
        self.info.update(keys)
        self.player.update(keys)

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.info.draw(surface)
        self.player.draw(surface)

    def setup_player(self):
        self.player = player.Player('mario')
        self.player.rect.x = 300
        self.player.rect.y = 490