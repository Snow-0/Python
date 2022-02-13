# import pygame library and random module
import pygame
import random
from pygame.locals import *
from pygame.math import Vector2

# initialize pygame
pygame.init()

# Declare variables
# screen size
cell_size = 40
cell_number = 20
fps = 60
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
# define font
font_counter = pygame.font.SysFont("Fira Code", 60)
font_restart = pygame.font.SysFont("Fira Code", 30)

# define color
WHITE = (255, 255, 255)
SNAKE_COLOR = (0, 255, 0)  # Green
APPLE_COLOR = (255, 0, 0)  # Red
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake")
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


class Snake:
    def __init__(self):
        # starting snake size
        self.body = [
            Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)

        ]
        self.direction = Vector2(0, 0)
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
        # adds new block to end of snake when eating apple
        if self.new_block == True:
            body_copy = self.body[:]  # copies entire snake.body list
            # adds snake head to the front of the list + direction of input
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]  # updates the new snake body size
            self.new_block = False
        # moves snake without adding a block
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    # resets position of snake when colliding with itself or wall
    def reset(self):

        self.body = [
            Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)

        ]
        self.direction = Vector2(0, 0)


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

            # add block to snake
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.apple.pos:
                self.apple.randomize()

    def check_fail(self):
        # check if snake leaves the screen
        if not 0 <= self.snake.body[0].x <= cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y <= cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()


main_game = Main()

# Main game loop
run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(fps)
    screen.fill(BLACK)

    # draws the score
    counter = str(len(main_game.snake.body) - 3)
    draw_text(str(counter), font_counter, WHITE,
              (cell_size * cell_number / 2 - 10), 5)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == KEYDOWN:
            # checks if user input is the arrow keys
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                key = pygame.key.name(event.key)
                if key == "up":
                    # prevents user from moving back into the snake's body
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
