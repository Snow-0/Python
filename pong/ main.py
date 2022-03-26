import pygame
from pygame.locals import *
pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600

# Declare variables
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

VEL = 0.5
paddle_a_y_pos = 250
paddle_b_y_pos = 250
paddle_a_input = ""
paddle_b_input = ""  

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
    
    def draw_ball(self):
        pass    
    
class Main: 
    # initializes paddles and ball 
    def __init__(self):
        self.paddle_a = Paddle()
        self.paddle_b = Paddle()
    # Draws the items in the game
    def draw_elements(self):
        self.paddle_a.draw_paddle(100, paddle_a_y_pos)
        self.paddle_b.draw_paddle(900, paddle_b_y_pos)
        pygame.draw.line(screen, WHITE, (500, 0), (500, 600), width=20)

    def move_paddle_a(self):

        global paddle_a_y_pos 
        if paddle_a_input == "w":
            paddle_a_y_pos -= VEL
    
        if paddle_a_input == "s":
            paddle_a_y_pos += VEL
    
    def move_paddle_b(self):
        global paddle_b_y_pos

        if paddle_b_input == "up":
            paddle_b_y_pos -= VEL
            
        if paddle_b_input == "down":
            paddle_b_y_pos += VEL

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
   
    screen.fill(BLACK)  
    main.draw_elements() 
    pygame.display.update()

pygame.quit()