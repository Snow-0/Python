# basic code for pygame

import pygame
import sys

# initialize pygame
pygame.init()
clock = pygame.time.Clock()

# window size
screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Paddle:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 10
        self.height = 140
        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
        self.speed = 0

    def draw_paddle(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def paddle_movement(self):
        self.rect.y += self.speed

        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= screen_height:
            self.rect.y = screen_height


paddle_a = Paddle(10, screen_height / 2 - 70)
paddle_b = Paddle(screen_width - 20, screen_height / 2 - 70)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # player keys
            if event.key == pygame.K_DOWN:
                paddle_b.speed += 10
            if event.key == pygame.K_UP:
                paddle_b.speed -= 10

            # opponent movement
            if event.key == pygame.K_s:
                paddle_a.speed += 10
            if event.key == pygame.K_w:
                paddle_a.speed -= 10

        if event.type == pygame.KEYUP:
            # player movement
            if event.key == pygame.K_DOWN:
                paddle_b.speed -= 10
            if event.key == pygame.K_UP:
                paddle_b.speed += 10
            # opponent movement
            if event.key == pygame.K_s:
                paddle_a.speed -= 10
            if event.key == pygame.K_w:
                paddle_a.speed += 10

    screen.fill(BLACK)
    print(paddle_a.rect.y)
    paddle_a.draw_paddle()
    paddle_b.draw_paddle()
    paddle_a.paddle_movement()
    paddle_b.paddle_movement()
    # updating the window
    pygame.display.flip()
    clock.tick(60)
