import pygame
from pygame.locals import *
import random

pygame.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 600
SNAKE_COLOR = (0, 255, 0)
VEL = 5
fps = 60
clock = pygame.time.Clock()
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        # create surface of the snake
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(SNAKE_COLOR)
        self.vel = 5
        # gets the rectangle
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_dir = ""

        # Draws rectangle
        # pygame.draw.rect(screen, SNAKE_COLOR, (self.x, self.y, self.width, self.height))

    def border_collision(self):
        if snake.move_dir == "left" and snake.rect.x - VEL > 0:
            snake.rect.x -= VEL
        if snake.move_dir == "right" and snake.rect.x + VEL + snake.width < 600:
            snake.rect.x += VEL
        if snake.move_dir == "up" and snake.rect.y - VEL > 0:
            snake.rect.y -= VEL
        if snake.move_dir == "down" and snake.rect.y + VEL + snake.height < 700:
            snake.rect.y += VEL


# Snake
snake_group = pygame.sprite.Group()
snake = Snake(100, int(SCREEN_HEIGHT / 2), 20, 20)
snake_group.add(snake)


# Main game loop
run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(fps)
    screen.fill(BLACK)
    snake_group.draw(screen)

    snake.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.QUIT()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            # prevent diagonal movement
            # https://stackoverflow.com/questions/60252752/i-want-to-prevent-diagonal-movement-in-pygame
            elif event.key in [
                pygame.K_RIGHT,
                pygame.K_LEFT,
                pygame.K_UP,
                pygame.K_DOWN,
            ]:
                snake.move_dir = pygame.key.name(event.key)

    snake.border_collision()

    pygame.display.update()


pygame.quit()
