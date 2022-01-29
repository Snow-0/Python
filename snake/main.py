import pygame
from pygame.locals import *
import random

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


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


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
        # gets the rectangle
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_dir = ""

    def border_collision(self):
        if self.move_dir == "left" and self.rect.x - VEL > 0:
            self.rect.x -= VEL
        if self.move_dir == "right" and self.rect.x + VEL + self.width < 600:
            self.rect.x += VEL
        if self.move_dir == "up" and self.rect.y - VEL > 0:
            self.rect.y -= VEL
        if self.move_dir == "down" and self.rect.y + VEL + self.height < 700:
            self.rect.y += VEL


class Apple(Snake):
    def __init__(self, x, y, width, height):
        Snake.__init__(self, x, y, width, height)
        self.image.fill(APPLE_COLOR)


# Snake
snake_group = pygame.sprite.Group()
snake = Snake(100, int(SCREEN_HEIGHT / 2), 20, 20)
snake_group.add(snake)

# Apple
apple_group = pygame.sprite.Group()
apple = Apple(500, int(SCREEN_HEIGHT / 2), 20, 20)
apple_group.add(apple)


# Main game loop
run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(fps)

    screen.fill(BLACK)
    snake_group.draw(screen)
    snake.update()
    apple_group.draw(screen)
    apple.update()

    if pygame.sprite.groupcollide(snake_group, apple_group, False, True):
        score += 1
        apple = Apple(random.randint(0, 550), random.randint(0, 650), 20, 20)
        apple_group.add(apple)
    draw_text(str(score), font, white, int(SCREEN_WIDTH / 2 - 25), 20)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.QUIT()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            # prevent diagonal movement
            # https://stackoverflow.com/questions/60252752/i-want-to-prevent-diagonal-movement-in-pygame
            elif (
                event.key
                in [
                    pygame.K_RIGHT,
                    pygame.K_LEFT,
                    pygame.K_UP,
                    pygame.K_DOWN,
                ]
                and game_over == False
            ):
                snake.move_dir = pygame.key.name(event.key)

    snake.border_collision()

    pygame.display.update()


pygame.quit()
