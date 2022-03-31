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
screen_rect = screen.get_rect()
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
        self.score = 0

    def paddle_movement(self):
        pygame.draw.rect(screen, WHITE, self.rect)
        self.rect.y += self.speed

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

class Ball:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.ball_x_speed = 7
        self.ball_y_speed = 7
        
    def ball_bounce(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

        self.rect.x += self.ball_x_speed
        self.rect.y += self.ball_y_speed

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.ball_y_speed *= -1
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.ball_x_speed *= -1 
        
        if self.rect.colliderect(paddle_a.rect) or self.rect.colliderect(paddle_b.rect):
                self.ball_x_speed *= -1 
                
        


paddle_a = Paddle(10, screen_height / 2 - 70)
paddle_b = Paddle(screen_width - 20, screen_height / 2 - 70)
ball = Ball(screen_width/2 - 15, screen_height/2)



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

    # prevent white "trail"
    screen.fill(BLACK)
    # paddle movement
    paddle_a.paddle_movement()
    paddle_b.paddle_movement()
    # ball movement
    ball.ball_bounce()
# updating the window
    pygame.display.flip()
    clock.tick(60)
