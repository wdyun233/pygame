import pygame
from . import coin
pygame.font.init()


def create_label(label, size=40, width_scale=1.25, height_scale=1):
    font = pygame.font.SysFont('FixedSys.ttf', size)
    label_image = font.render(label, 0, (255, 255, 255))
    return label_image;


class Info:
    def __init__(self, state):
        self.state = state
        self.state_labels = []
        self.create_state_labels()
        self.create_info_labels()
        self.flash_coin = coin.FlashingCoin()

    def create_state_labels(self):
        if self.state == 'main_menu':
            self.state_labels.append((create_label('1 PLAYER GAME'), (272, 360)))
            self.state_labels.append((create_label('2 PLAYER GAME'), (272, 405)))
            self.state_labels.append((create_label('TOP - '), (272, 465)))
            self.state_labels.append((create_label('0000000'), (350, 465)))
        elif self.state == 'load_screen':
            self.state_labels.append((create_label('WORLD'), (280, 200)))
            self.state_labels.append((create_label('1  -  1'), (430, 200)))
            self.state_labels.append((create_label('x    3'), (380, 280)))
        elif self.state == 'level':
            pass

    def create_info_labels(self):
        self.state_labels.append((create_label('MARIO'), (75, 30)))
        self.state_labels.append((create_label('WORLD'), (450, 30)))
        self.state_labels.append((create_label('TIME'), (625, 30)))
        self.state_labels.append((create_label('000000'), (75, 55)))
        self.state_labels.append((create_label('x00'), (300, 55)))
        self.state_labels.append((create_label('1  -  1'), (480, 55)))

    def update(self, keys):
        if self.state == 'main_menu':
            self.flash_coin.update()
        elif self.state == 'load_screen':
            pass
        elif self.state == 'level':
            pass

    def draw(self, surface):
        for label in self.state_labels:
            surface.blit(label[0], label[1])
        surface.blit(self.flash_coin.image, (self.flash_coin.rect.x, self.flash_coin.rect.y))
