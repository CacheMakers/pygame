import pygame
from math import sqrt
from random import randint

# These variables store the size of our window. Refer to them
# as often as possible, rather than just using the values
WIDE = 600
HIGH = 400

# starts everything up, creates our screen (window)
pygame.init()
screen = pygame.display.set_mode([WIDE,HIGH])
pygame.display.set_caption("Shooter")

clock = pygame.time.Clock()

# player location - starts in the center of the screen
player_x = WIDE//2
player_y = HIGH//2

# player speed
player_speed = 5

# location of aim reticule
aim_x = 30
aim_y = 0

# bullets
bullets = []
fire = False

running = True
# this loop runs until the game exits
while running:
    ## handle input ##
    for event in pygame.event.get():
        # quit game - this triggers when you click the x or press alt+f4
        if event.type == pygame.QUIT:
            running = False
        # fires a bullet
        if event.type == pygame.MOUSEBUTTONDOWN:
            fire = True
    
    # move player
    player_input = pygame.key.get_pressed()
    if player_input[pygame.K_UP] or player_input[pygame.K_w]:
        player_y -= player_speed
    if player_input[pygame.K_RIGHT] or player_input[pygame.K_d]:
        player_x += player_speed
    if player_input[pygame.K_DOWN] or player_input[pygame.K_s]:
        player_y += player_speed
    if player_input[pygame.K_LEFT] or player_input[pygame.K_a]:
        player_x -= player_speed

    ## game logic ##
    # place aim reticule
    mouse_x,mouse_y = pygame.mouse.get_pos()
    aim_x = mouse_x-player_x
    aim_y = mouse_y-player_y
    mouse_dist = sqrt(aim_x**2+aim_y**2)
    aim_x = int(aim_x/mouse_dist*30)
    aim_y = int(aim_y/mouse_dist*30)

    # add a new bullet to the list
    if fire == True:
        bullets.append([player_x,player_y,aim_x//2,aim_y//2])
        fire = False

    # move the bullets, and delete them if they leave the screen
    temp = []
    for bullet in bullets:
        bullet[0] += bullet[2]
        bullet[1] += bullet[3]
        if -50 <= bullet[0] <= WIDE+50 and -50 <= bullet[1] <= HIGH+50:
            temp.append(bullet)
    bullets = temp

    ## draw screen ##
    screen.fill((150,150,255))
    for bullet in bullets:
        pygame.draw.circle(screen, (255,255,0), (bullet[0],bullet[1]),5)
    pygame.draw.circle(screen, (0,0,255), (player_x,player_y), 20)
    pygame.draw.circle(screen, (0,0,255), (player_x+aim_x,player_y+aim_y), 5)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
