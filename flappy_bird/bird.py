import pygame
import os


PATH = 'flappy_bird/assets/sprites/'


class Bird(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        self.sprites.append(pygame.image.load(
            os.path.join(PATH, 'redbird-upflap.png')))
        self.sprites.append(pygame.image.load(
            os.path.join(PATH, 'redbird-downflap.png')))
        self.sprites.append(pygame.image.load(
            os.path.join(PATH, 'redbird-midflap.png')))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def move(self, pixel):
        self.rect.y = max([self.rect.y - pixel, 0])

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

        self.image = self.sprites[int(self.current_sprite)]
