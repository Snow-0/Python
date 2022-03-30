import pygame
import sys
import random

# initialize pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

# window size
screen_width = 1280
screen_height = 960

# ball speed
ball_speed_x, ball_speed_y = 7, 7

player_speed = 0
opponent_speed = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# game rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)


# score
font = pygame.font.SysFont('monospace', 30)
player_score = 0
opponent_score = 0


def ball_bounce():
    global ball_speed_x, ball_speed_y, opponent_score, player_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        if ball.left <= 0:
            player_score += 1
            print(player_score)
        if ball.right >= screen_width:
            opponent_score += 1
        ball_restart()

    # paddle collision
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))


def player_movement():
    # allow the player paddle to move
    player.y += player_speed

    # check if paddle leaves the screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_movement():
    # allow the opponent paddle to move
    opponent.y += opponent_speed

    # check if paddle leaves the screen
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def draw_score():
    player_score_text = font.render(str(player_score), 1, WHITE)
    opponent_score_text = font.render(str(opponent_score), 1, WHITE)
    screen.blit(player_score_text, (screen_width / 2 + 15, screen_height / 2))
    screen.blit(opponent_score_text,
                (screen_width / 2 - 35, screen_height / 2))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # player keys
            if event.key == pygame.K_DOWN:
                player_speed += 10
            if event.key == pygame.K_UP:
                player_speed -= 10

            # opponent movement
            if event.key == pygame.K_s:
                opponent_speed += 10
            if event.key == pygame.K_w:
                opponent_speed -= 10

        if event.type == pygame.KEYUP:
            # player movement
            if event.key == pygame.K_DOWN:
                player_speed -= 10
            if event.key == pygame.K_UP:
                player_speed += 10
            # opponent movement
            if event.key == pygame.K_s:
                opponent_speed -= 10
            if event.key == pygame.K_w:
                opponent_speed += 10

    # prevents 'trail'
    screen.fill(BLACK)
    player_movement()
    opponent_movement()
    ball_bounce()
    draw_score()
    print(player.y)
    # draws paddles and ball
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    # draws the line
    pygame.draw.aaline(screen, WHITE, (screen_width / 2, 0),
                       (screen_width / 2, screen_height))

    # updating the window
    pygame.display.flip()
    clock.tick(60)
