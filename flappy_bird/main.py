import pygame
from pygame.locals import *
import os


clock = pygame.time.Clock()
FPS = 60

pygame.init()

SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")


# Game Variables
ground_scroll = 0
scroll_speed = 4

# load images
bg = pygame.image.load(os.path.join("flappy_bird/img", "bg.png"))
base = pygame.image.load(os.path.join("flappy_bird/img", "ground.png"))
# Scale the image to window size

# creates the bird by inheriting pygame.sprite.Sprite
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("flappy_bird/img/bird1.png")
        # creates a rectangle from the boundmaries of the image
        self.rect = self.image.get_rect()
        # centers the rectangle
        self.rect.center = [x, y]


bird_group = pygame.sprite.Group()
# positions flappy on the screen
flappy = Bird(100, int(SCREEN_HEIGHT / 2))

bird_group.add(flappy)


run = True
while run:

    clock.tick(FPS)
    screen.blit(bg, (0, 0))

    bird_group.draw(screen)

    # draw and scroll
    screen.blit(base, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    # Must be included
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
