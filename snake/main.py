import pygame
import random
from pygame.locals import *
from pygame.math import Vector2

pygame.init()

cell_size = 40
cell_number = 20
SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)
fps = 60
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
game_over = False
# define font
font = pygame.font.SysFont("Fira Code", 60)
score = 0
# define color
white = (255, 255, 255)
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake")
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
counter = 0


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


class Snake:
    def __init__(self):

        self.body = [
            Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)

        ]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            # create rect
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # Draw rect
            pygame.draw.rect(screen, SNAKE_COLOR, snake_rect)

    def move(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class Apple:
    def __init__(self):
        self.randomize()

    def draw_apple(self):
        apple_rect = pygame.Rect(
            int(self.x * cell_size), int(self.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, APPLE_COLOR, apple_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()

    def update(self):
        self.snake.move()
        self.check_collision()

    def draw_elements(self):
        self.snake.draw_snake()
        self.apple.draw_apple()

    def check_collision(self):
        global counter
        if self.apple.pos == self.snake.body[0]:
            # repositions the fruit
            self.apple.randomize()
            counter += 1

            # add block to snake
            self.snake.add_block()

    def check_fail(self):
        # check if snake leaves the screen
        if not 0 <= self.snake.body[0].x <= cell_number - 1:
            self.game_over()
        if not 0 <= self.snake.body[0].y <= cell_number - 1:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.QUIT()


main_game = Main()

# Main game loop
run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(fps)

    screen.fill(BLACK)
    draw_text(str(counter), font, white, (cell_size * cell_number / 2 - 10), 5)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == KEYDOWN and game_over == False:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                key = pygame.key.name(event.key)
                if key == "up":
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                elif key == "down":
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                elif key == "left":
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
                elif key == "right":
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
    main_game.check_fail()
    main_game.draw_elements()
    pygame.display.update()


pygame.quit()
