import pygame
from pygame.locals import *



pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600

# Declare variables
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# speed the paddle move when key is pressed
VEL = 8

# initial positions for paddle a and b
paddle_a_x_pos = 100
paddle_a_y_pos = 250
paddle_b_x_pos = 900
paddle_b_y_pos = 250
paddle_a_input = ""
paddle_b_input = ""
ball_x_pos = 450
ball_y_pos = 450
x_speed, y_speed = 4, 4

ball_rect = pygame.Rect(ball_x_pos, ball_y_pos, 20, 20)
pygame.draw.rect(screen, WHITE, ball_rect)
clock = pygame.time.Clock()

class Paddle:
    
    def __init__(self):
        self.width = 20
        self.height = 100
    
    def draw_paddle(self, x_pos, y_pos):
        paddle_rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
        pygame.draw.rect(screen, WHITE, paddle_rect)

class Ball:
    def __init__(self):
        self.width = 20
        self.height = 20
    
    def draw_ball(self, ball_x_pos, ball_y_pos):
        # global ball_rect
        # ball_rect = pygame.Rect(ball_x_pos, ball_y_pos, self.width, self.height)
        pygame.draw.rect(screen, WHITE, ball_rect)
    
class Main: 
    # initializes paddles and ball 
    def __init__(self):
        self.paddle_a = Paddle()
        self.paddle_b = Paddle()
        self.ball = Ball()
    # Draws the items in the game
    def draw_elements(self):
        self.paddle_a.draw_paddle(paddle_a_x_pos, paddle_a_y_pos)
        self.paddle_b.draw_paddle(paddle_b_x_pos, paddle_b_y_pos)
        self.ball.draw_ball(ball_x_pos, ball_y_pos)
        pygame.draw.line(screen, WHITE, (500, 0), (500, 600), width=20)


    def move_paddle_a(self):
        global paddle_a_y_pos 
        if paddle_a_input == "w" and paddle_a_y_pos - VEL > 0:
            paddle_a_y_pos -= VEL
    
        if paddle_a_input == "s" and paddle_a_y_pos + VEL + main.paddle_a.height < SCREEN_HEIGHT:
            paddle_a_y_pos += VEL
    
    def move_paddle_b(self):
        global paddle_b_y_pos

        if paddle_b_input == "up" and paddle_b_y_pos - VEL > 0:
            paddle_b_y_pos -= VEL
            
        if paddle_b_input == "down" and paddle_b_y_pos + VEL + main.paddle_a.height < SCREEN_HEIGHT:
            paddle_b_y_pos += VEL
    
    def collision(self):
        global x_speed, y_speed

        ball_rect.x += x_speed
        ball_rect.y += y_speed

        # collision with the borders
        if ball_rect.right >= SCREEN_WIDTH  or ball_rect.left <= 0:
            x_speed *= -1
        
        if ball_rect.bottom >= SCREEN_HEIGHT  or ball_rect.top <=0:
            y_speed *= -1
        

# instantiate main object
main = Main()

# main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    # paddle A movment
    if keys[pygame.K_w]:
        paddle_a_input = "w" 
        main.move_paddle_a()
    if keys[pygame.K_s]:
        paddle_a_input = "s" 
        main.move_paddle_a()

    # paddle B movement
    if keys[pygame.K_UP]:
        paddle_b_input = "up" 
        main.move_paddle_b()
    if keys[pygame.K_DOWN]:
        paddle_b_input = "down"
        main.move_paddle_b()
    
    # fills the screen with the color black when the paddles move
    # prevents a white "trail"
    screen.fill(BLACK)  
    # draws items onto the screen
    main.draw_elements() 
    main.collision()
    pygame.display.update()
    # sets the game to a constant 60 fps 
    clock.tick(60)

pygame.quit()