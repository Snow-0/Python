import pygame

BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.height = height

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
    # source: https://stackoverflow.com/questions/31599162/how-to-create-a-border-in-pygame

    def move_up(self, pixel):
        self.rect.y = max([self.rect.y - pixel, 0])

    def move_down(self, pixel):
        self.rect.y = min([self.rect.y + pixel, 700 - self.height])
