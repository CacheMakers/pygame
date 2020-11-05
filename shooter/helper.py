import math
import pygame

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
