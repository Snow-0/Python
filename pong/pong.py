# Pong clone using the Pygame library
# followed this for countdown timer: https://www.youtube.com/watch?v=E4Ih9mpn5tk
# followed this for rectangle collision: https://www.youtube.com/watch?v=W9uKzPFS1CI


import pygame
import random
import sys

# initialize pygame
pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('monospace', 40)

# window size
screen_width = 1280
screen_height = 960

# setting the window size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# paddle color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# score timer
score_timer = None


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
        self.rect = pygame.Rect(self.x_pos, self.y_pos,
                                self.width, self.height)
        self.ball_x_speed = 10
        self.ball_y_speed = 10
        self.collision_tolerance = 20
        self.score_time = None
        self.current_time = None

    def ball_bounce(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

        self.rect.x += self.ball_x_speed
        self.rect.y += self.ball_y_speed

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.ball_y_speed *= -1
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            # adds a point when ball hits the left or right border
            self.paddle_score()

        # collision with the paddles
        if self.rect.colliderect(paddle_a.rect):
            if abs(paddle_a.rect.top - self.rect.bottom) < self.collision_tolerance:
                self.ball_y_speed *= -1
            if abs(paddle_a.rect.bottom - self.rect.top) < self.collision_tolerance:
                self.ball_y_speed *= -1
            if abs(paddle_a.rect.right - self.rect.left) < self.collision_tolerance:
                self.ball_x_speed *= -1
            if abs(paddle_a.rect.left - self.rect.right) < self.collision_tolerance:
                self.ball_x_speed *= -1
        if self.rect.colliderect(paddle_b.rect):
            if abs(paddle_b.rect.top - self.rect.bottom) < self.collision_tolerance:
                self.ball_y_speed *= -1
            if abs(paddle_b.rect.bottom - self.rect.top) < self.collision_tolerance:
                self.ball_y_speed *= -1
            if abs(paddle_b.rect.right - self.rect.left) < self.collision_tolerance:
                self.ball_x_speed *= -1
            if abs(paddle_b.rect.left - self.rect.right) < self.collision_tolerance:
                self.ball_x_speed *= -1

    def reset(self):
        self.current_time = pygame.time.get_ticks()
        # positions the ball in the middle
        self.rect.center = (screen_width / 2, screen_height / 2)

        if self.current_time - self.score_time < 700:
            three = font.render('3', True, WHITE)
            screen.blit(three, (screen_width / 2 -
                        10, screen_height / 2 + 20))
        if 700 < self.current_time - self.score_time < 1400:
            two = font.render('2', True, WHITE)
            screen.blit(two, (screen_width / 2 -
                        10, screen_height / 2 + 20))

        if self.current_time - self.score_time < 2100:
            one = font.render('1', True, WHITE)
            screen.blit(one, (screen_width / 2 -
                        10, screen_height / 2 + 20))
        if self.current_time - self.score_time < 2100:
            self.ball_x_speed, self.ball_y_speed = 0, 0
        else:
            # causes the ball to come out in a random direction
            self.ball_x_speed = 7 * random.choice((1, -1))
            self.ball_y_speed = 7 * random.choice((1, -1))
            self.score_time = None

    def paddle_score(self):
        if self.rect.left <= 0:
            paddle_a.score += 1
            self.score_time = pygame.time.get_ticks()
        if self.rect.right >= screen_width:
            paddle_b.score += 1
            self.score_time = pygame.time.get_ticks()


paddle_a = Paddle(10, screen_height / 2 - 70)
paddle_b = Paddle(screen_width - 20, screen_height / 2 - 70)
ball = Ball(screen_width/2 - 15, screen_height/2)


def draw_score():
    paddle_a_score_text = font.render(str(paddle_a.score), 1, WHITE)
    paddle_b_score_text = font.render(str(paddle_b.score), 1, WHITE)
    screen.blit(paddle_a_score_text,
                (screen_width / 2 + 15, screen_height / 2))
    screen.blit(paddle_b_score_text,
                (screen_width / 2 - 40, screen_height / 2))


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
    # draws the in line in the middle
    pygame.draw.aaline(screen, WHITE, (screen_width / 2, 0),
                       (screen_width / 2, screen_height))
    if ball.score_time:
        # resets the ball to the middle when the ball hits the left or right border
        ball.reset()
    # ball movement
    ball.ball_bounce()
    # draws paddle scores
    draw_score()
    # updating the window
    pygame.display.flip()
    clock.tick(60)
