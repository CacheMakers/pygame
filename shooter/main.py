import pygame
from math import sqrt
from math import sin, cos
from random import randint

def dist(x1,y1,x2,y2):
    answ = sqrt((x1-x2)**2+(y1-y2)**2)
    if answ == 0:
        print("problem")
    return answ

# These variables store the size of our window. Refer to them
# as often as possible, rather than just using the values
WIDE = 600
HIGH = 400

# starts everything up, creates our screen (window)
pygame.init()
screen = pygame.display.set_mode([WIDE,HIGH])
pygame.display.set_caption("Shooter")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial",30)

# player location - starts in the center of the screen
player_x = WIDE//2
player_y = HIGH//2

# player speed
player_speed = 5
dead = False

# location of aim reticule
aim_x = 30
aim_y = 0

# bullets
bullets = []
fire = False

# targets and score
targets = []
score = 0
target_speed = 2

# stars
stars = []
for i in range(30):
    stars.append([randint(0,WIDE),randint(0,HIGH)])

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and dead == True:
                targets = []
                bullets = []
                score = 0
                player_x = WIDE//2
                player_y = HIGH//2
                dead = False
    
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
    mouse_dist = dist(0,0,aim_x,aim_y)
    aim_x = int(aim_x/mouse_dist*30)
    aim_y = int(aim_y/mouse_dist*30)

    # add a new bullet to the list
    if fire == True:
        bullets.append([player_x,player_y,aim_x//2,aim_y//2])
        fire = False

    # move the bullets, and delete them if they leave the screen
    alive_bullets = []
    for bullet in bullets:
        bullet[0] += bullet[2]
        bullet[1] += bullet[3]
        if -50 <= bullet[0] <= WIDE+50 and -50 <= bullet[1] <= HIGH+50:
            alive_bullets.append(bullet)
    bullets = alive_bullets

    # randomly add an enemy
    chance = randint(0,180)
    vel = randint(-5,5)
    if chance == 0:     # from the top
        targets.append([randint(0,WIDE),-30,vel,target_speed])
    if chance == 1:     # from the right
        targets.append([WIDE+30,randint(0,HIGH),-target_speed,vel])
    if chance == 2:     # from the bottom
        targets.append([randint(0,WIDE),HIGH+30,vel,-target_speed])
    if chance == 3:     # from the left
        targets.append([-30,randint(0,HIGH),target_speed,vel])

    # move the enemies, delete them if they leave the screen or hit a bullet
    alive_targets = []
    for target in targets:
        target[0] += target[2]
        target[1] += target[3]
        hit = False
        alive_bullets = []
        for bullet in bullets:
            if dist(bullet[0],bullet[1],target[0],target[1]) <= 30:
                hit = True
                score += 1
            else:
                alive_bullets.append(bullet)
        bullets = alive_bullets
        if -50 <= target[0] <= WIDE+50 and -50 <= target[1] <= HIGH+50 and not hit:
            alive_targets.append(target)
        if dist(target[0],target[1],player_x,player_y) <= 50:
            dead = True
    targets = alive_targets

    ## draw screen ##
    screen.fill((0,0,0))
    if not dead:
        for star in stars:
            pygame.draw.circle(screen, (150,150,0), (star[0],star[1]),randint(1,3))
        for bullet in bullets:
            pygame.draw.circle(screen, (255,255,0), (bullet[0],bullet[1]),5)
        for target in targets:
            pygame.draw.circle(screen, (255,0,0), (target[0],target[1]),30)
        pygame.draw.circle(screen, (0,0,255), (player_x,player_y), 20)
        pygame.draw.circle(screen, (0,0,255), (player_x+aim_x,player_y+aim_y), 5)
    else:
        screen.blit(font.render("You are dead!", True, (255,255,0)),(150,150))    
        screen.blit(font.render("Your score: "+str(score), True, (255,255,0)),(150,190))    
        screen.blit(font.render("Press Enter to try again", True, (255,255,0)),(150,350))    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
