import pygame
from .. import setup, tools, constants as C
import json
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.load_data()
        self.setup_status()
        self.setup_timers()
        self.setup_velocities()
        self.load_image()
        self.state = 'stand'

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def load_data(self):
        file_name = self.name + '.json'
        file_path = os.path.join('source/data/player', file_name)
        with open(file_path) as f:
            self.player_data = json.load(f)

    def handle_state(self, keys):
        if self.state == 'stand':
            self.stand(keys)
        if self.state == 'walk':
            self.walk(keys)
        if self.state == 'jump':
            self.jump(keys)
        if self.state == 'basketball':
            self.basketball(keys)
        if self.face_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]

    def stand(self, keys):
        self.x_vel = 0
        self.y_vel = 0
        self.frame_index = 0
        if keys[pygame.K_RIGHT]:
            self.face_right = True
            self.state = 'walk'
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            self.state = 'walk'
    def walk(self, keys):
        self.max_x_vel = self.max_walk_vel
        self.x_accel = self.walk_accel
        if pygame.time.get_ticks() - self.walking_timer > 100:
            self.walking_timer = pygame.time.get_ticks()
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 1
        if keys[pygame.K_RIGHT]:
            self.face_right = True
            if self.x_vel < 0:
                self.frame_index = 5
                self.x_accel = self.turn_accel
            self.x_vel = self.cale_val()
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            if self.x_vel > 0:
                self.frame_index = 5
                self.x_accel = self.turn_accel
            self.x_vel = self.cale_val()

        else:
            if self.face_right:
                self.x_vel -= self.x_accel
                if self.x_vel <= 0:
                    self.x_vel = 0
                    self.state = 'stand'
            else:
                self.x_vel += self.x_accel
                if self.x_vel >= 0:
                    self.x_vel = 0
                    self.state = 'stand'

    def jump(self, keys):
        pass

    def basketball(self, keys):
        pass

    def cale_val(self):
        if self.face_right:
            return min(self.x_vel + self.x_accel, self.max_x_vel)
        else:
            return max(self.x_vel - self.x_accel, -self.max_x_vel)
    def update(self, keys):
        self.handle_state(keys)

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0
        speed = self.player_data['speed']
        self.max_walk_vel = speed['max_walk_speed']
        self.max_run_vel = speed['max_run_speed']
        self.max_y_vel = speed['max_y_velocity']
        self.jump_vel = speed['jump_velocity']
        self.walk_accel = speed['walk_accel']
        self.run_accel = speed['run_accel']
        self.turn_accel = speed['turn_accel']
        self.gravity = C.GRAVITY

        self.max_x_vel = self.max_walk_vel
        self.x_accel = self.walk_accel

    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def setup_status(self):
        self.face_right = True
        self.dead = False
        self.big = False

    def load_image(self):
        sheet = setup.GRAPHICS['mario_bros']
        frame_rects = self.player_data['image_frames']
        self.frames = []
        self.right_small_normal_frams = []
        self.right_big_normal_frams = []
        self.right_big_fire_frams = []
        self.left_small_normal_frams = []
        self.left_big_normal_frams = []
        self.left_big_fire_frams = []

        self.small_normal_frams = [self.right_small_normal_frams, self.left_small_normal_frams]
        self.big_normal_frams = [self.right_big_normal_frams, self.left_big_normal_frams]
        self.big_fire_frams = [self.right_big_fire_frams, self.left_big_fire_frams]
        self.all_frams = [
            self.right_small_normal_frams,
            self.right_big_normal_frams,
            self.right_big_fire_frams,
            self.left_small_normal_frams,
            self.left_big_normal_frams,
            self.left_big_fire_frams
        ]

        for group, group_frame_rect in frame_rects.items():
            for frame_rect in group_frame_rect:
                right_image = tools.get_image(sheet, frame_rect['x'], frame_rect['y'], frame_rect['width'],
                                              frame_rect['height'], (0, 0, 0), C.PLAYER_MULTI)
                left_image = pygame.transform.flip(right_image, True, False)
                if group == 'right_small_normal':
                    self.right_small_normal_frams.append(right_image)
                    self.left_small_normal_frams.append(left_image)
                if group == 'right_big_normal':
                    self.right_big_normal_frams.append(right_image)
                    self.left_big_normal_frams.append(left_image)
                if group == 'right_big_fire':
                    self.right_big_fire_frams.append(right_image)
                    self.left_big_fire_frams.append(left_image)

        self.right_frames = self.right_small_normal_frams
        self.left_frames = self.left_small_normal_frams
        self.frames = self.right_frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update_frame(self):
        if self.state == 'jump':
            self.image = self.frames[4]
            return
        now = pygame.time.get_ticks()
        if self.walking_timer == 0:
            self.walking_timer = now
        if now - self.walking_timer > 100:
            self.frame_index += 1
            self.frame_index %= 4
            self.walking_timer = 0
        self.image = self.frames[self.frame_index]
