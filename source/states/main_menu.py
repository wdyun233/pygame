import pygame

from .. import setup
from .. import constants as C
from .. import tools
from ..components import info


class MainMenu:

    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.next = 'load_screen'
        self.state_name = 'main_menu'
        self.info = info.Info(self.state_name)
        self.finished = False

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (rect.width*2.68, rect.height*2.68))
        self.viewport = setup.SCREEN.get_rect()
        self.caption = tools.get_image(setup.GRAPHICS['title_screen'], 1, 60, 176, 88, (255, 0, 220), C.BG_MULTI)

    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        self.cursor.image = tools.get_image(setup.GRAPHICS['item_objects'], 24, 160, 8, 8, (0, 0, 0), C.BG_MULTI)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (220, 360)
        self.cursor.rect = rect
        self.cursor.state = '1P'

    def update_cursor(self, keys):
        if keys[pygame.K_UP]:
            self.cursor.state = '1P'
            self.cursor.rect.y = 360
        elif keys[pygame.K_DOWN]:
            self.cursor.state = '2P'
            self.cursor.rect.y = 405
        elif keys[pygame.K_RETURN]:
            if self.cursor.state == '1P':
                self.finished = True
            else:
                self.finished = True

    def setup_player(self):
        self.player = tools.get_image(setup.GRAPHICS['mario_bros'], 178, 32, 12, 16, (0, 0, 0), C.PLAYER_MULTI)

    def update(self, keys):
        self.update_cursor(keys)
        self.info.update(keys)

    def draw(self, surface):
        surface.blit(self.background, self.viewport)
        surface.blit(self.caption, (170, 100))
        surface.blit(self.player, (110, 490))
        surface.blit(self.cursor.image, self.cursor.rect)
        self.info.draw(surface)
