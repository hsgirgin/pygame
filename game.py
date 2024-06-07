# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(60,390)
jump = 0
bef_jump = 0
rect_cord = 500
rect_cord1 = 500
rect_cord2 = 500
rect_cord3 = 500
rect_cord4 = 500
mult = 1
score = 0
x = 50
y = 300
m = 1
v = 5
jump = 0
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    text_surface = my_font.render(str(score), False, (0, 0, 0))
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")
    screen.blit(text_surface, (0,0))
    mult = random.randint(0,int(score/3+3))
    background = pygame.Rect(0,400,500,100)
    rectangle1 = pygame.Rect(rect_cord,360,40,40)
    rectangle2 = pygame.Rect(rect_cord1,360,40,40)
    pygame.draw.rect(screen, "green", background)
    pygame.draw.rect(screen, "yellow", rectangle1)
    pygame.draw.rect(screen, "black", rectangle2)
    pygame.draw.circle(screen, "red", player_pos, 10)
    # RENDER YOUR GAME HERE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if jump == 0:
            jump = 1
    if keys[pygame.K_DOWN]:
        jump = 0
        m = 1
        v = 5
        player_pos.y = 390
    while player_pos.y >= 390 and jump == 0:
       player_pos.y = player_pos.y - 1
    while player_pos.y <= 390 and jump == 0:
     player_pos.y = player_pos.y + 1
    # flip() the display to put your work on screen
    if jump == 1:
        k = 0.5 * m * v**2  # Calculate the vertical displacement
        player_pos.y -= k  # Update the sprite's vertical position
        v -= 0.2  # Simulate gravity by gradually decreasing velocity
        if v < 0:
            m = -1  # Change the direction of displacement for a realistic jump feel
        if v < -5:
            m = 1  # Reset parameters for subsequent jumps
            v = 5
            jump = 0  # Reset the jump flag upon completion
    rect_cord = rect_cord - mult
    rect_cord1 = rect_cord1 - mult*2
    if rect_cord < -40:
        rect_cord = 500
        rect_cord1 = 500
        score = score + 1
    if jump == 0 and ((player_pos.x <= rect_cord + 40 and player_pos.x >= rect_cord) or (player_pos.x >= rect_cord1 and player_pos.x <= rect_cord1+40)):
        score = 0
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()