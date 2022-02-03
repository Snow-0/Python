import pygame, random
from pygame.locals import *
from pygame.math import Vector2

pygame.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 600
SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)
VEL = 4
fps = 60
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
game_over = False
# define font
font = pygame.font.SysFont("Fira Code", 60)
score = 0
# define color
white = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


class Snake:
    def __init__(self):

        self.body = [
            Vector2(100, 300),
            Vector2(120, 300),
            Vector2(140, 300),
            Vector2(160, 300),
        ]
        self.direction = Vector2(10, 0)

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x
            y_pos = block.y
            # create rect
            snake_rect = pygame.Rect(x_pos, y_pos, 20, 20)
            # Draw rect
            pygame.draw.rect(screen, SNAKE_COLOR, snake_rect)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_apple(self):
        apple_rect = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.rect(screen, APPLE_COLOR, apple_rect)


# instantiate objects
# Apple
apple = Apple(500, SCREEN_HEIGHT // 2)
# Snake
snake = Snake()


class Main:
    def __init__(self):
        self.snake = Snake()


# Main game loop
run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(fps)

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.QUIT()
        if event.type == SCREEN_UPDATE:
            snake.move()
        if event.type == KEYDOWN:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                key = pygame.key.name(event.key)
                if key == "up":
                    snake.direction = Vector2(0, -15)
                elif key == "down":
                    snake.direction = Vector2(0, 15)
                elif key == "left":
                    snake.direction = Vector2(-15, 0)
                elif key == "right":
                    snake.direction = Vector2(15, 0)

    snake.draw_snake()
    apple.draw_apple()
    pygame.display.update()


pygame.quit()
