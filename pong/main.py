import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 900, 700

WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

BORDER = pygame.Rect(WIDTH // 2, 0, 10, HEIGHT)

paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 100
paddle1.rect.y = 200

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 750
paddle2.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

sprite_group = pygame.sprite.Group()
sprite_group.add(paddle1)
sprite_group.add(paddle2)
sprite_group.add(ball)


def window():
    paddle1_score = 0
    paddle2_score = 0
    WIN.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text = font.render(str(paddle1_score), 1, WHITE)
    WIN.blit(text, (250, 10))
    text = font.render(str(paddle2_score), 1, WHITE)
    WIN.blit(text, (420, 10))
    pygame.draw.line(WIN, WHITE, [450, 0], [450, 700], 10)
    if ball.rect.x >= 690:
        paddle1_score += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        paddle2_score += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
    sprite_group.draw(WIN)
    sprite_group.update()

    pygame.display.update()


def main():
    # Caps game to 60 fps
    clock = pygame.time.Clock()
    clock.tick(60)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()
        clock.tick(60)

        # Movement for paddle1
        if key_pressed[pygame.K_w]:
            paddle1.move_up(10)
        if key_pressed[pygame.K_s]:
            paddle1.move_down(10)
        # Movement for paddle2
        if key_pressed[pygame.K_UP]:
            paddle2.move_up(10)
        if key_pressed[pygame.K_DOWN]:
            paddle2.move_down(10)

        # Check if the ball is bouncing against any of the 4 walls:

        if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
            ball.bounce()

        window()

    pygame.quit()


if __name__ == "__main__":
    main()
