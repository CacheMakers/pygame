import math
import pygame
from random import randint

def rotate_texture(texture,angle,position):
    h = texture.get_rect().height//2
    w = texture.get_rect().width//2
    r = math.sqrt((w/2)**2 + (h/2)**2)
    a = math.radians(math.degrees(angle)%90)
    hn = h*math.sin(a)+w*math.cos(a)
    wn = h*math.cos(a)+h*math.sin(a)
    rn = math.sqrt(hn**2+wn**2)
    return pygame.transform.rotate(texture,math.degrees(angle)+180),(position[0]-(wn-w),position[1]-(hn-h))

def dist(x1,y1,x2,y2):
    answ = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if answ == 0:
        print("problem")
    return answ

def generate_target(HIGH, WIDE, target_speed, probability):
    chance = randint(0,probability*4)
    vel = randint(-5,5)
    if chance == 0:     # from the top
        return [randint(0,WIDE),-30,vel,target_speed]
    if chance == 1:     # from the right
        return [WIDE+30,randint(0,HIGH),-target_speed,vel]
    if chance == 2:     # from the bottom
        return [randint(0,WIDE),HIGH+30,vel,-target_speed]
    if chance == 3:     # from the left
        return [-30,randint(0,HIGH),target_speed,vel]
