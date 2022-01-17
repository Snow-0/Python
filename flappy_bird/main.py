import pygame
import os
from bird import Bird

WIDTH, HEIGHT = 500, 900


pygame.display.init()

WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))

FPS = 60

PATH = 'flappy_bird/assets/sprites/'

BG = pygame.transform.scale(pygame.image.load(os.path.join(
    PATH, 'background-day.png')), (WIDTH, HEIGHT))
BASE = pygame.transform.scale(pygame.image.load(
    os.path.join(PATH, 'base.png')), (900, 300))

bird = Bird(100, 450)
bird.pos_x = 10
bird.pos_y = 10

sprites = pygame.sprite.Group()
sprites.add(bird)


def draw():
    WIN.blit(BG, (0, 0))
    WIN.blit(BASE, (0, 750))

    sprites.draw(WIN)
    sprites.update()

    pygame.display.update()


def main():
    run = True

    # main loop
    while run:

        clock = pygame.time.Clock()
        clock.tick(FPS)
        key_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if key_pressed[pygame.K_SPACE]:
                bird.move(10)
                bird.animate()

        draw()


if __name__ == '__main__':
    main()
