import pygame
from pygame.locals import *

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

        # Draws rectangle
        # pygame.draw.rect(screen, SNAKE_COLOR, (self.x, self.y, self.width, self.height))

    def border_collision(self):
        pass


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
        print(snake.rect.x)

    if keys[pygame.K_LEFT]:
        snake.rect.x -= VEL
    if keys[pygame.K_RIGHT]:
        snake.rect.x += VEL
    if keys[pygame.K_UP]:
        snake.rect.y -= VEL
    if keys[pygame.K_DOWN]:
        snake.rect.y += VEL

    pygame.display.update()


pygame.quit()
