import pygame
import decimal
from pygame.locals import*
from random import*
import time

main = pygame.image.load('sprites/guy_white_shirt_brown_shorts.bmp')
main2 = pygame.image.load('sprites/guy_white_shirt_brown_shorts2.bmp')
main3 = pygame.image.load('sprites/guy_white_shirt_brown_shorts_back.bmp')
main4 = pygame.image.load('sprites/guy_white_shirt_brown_shorts_back2.bmp')
mainA11 = pygame.image.load('sprites/guy_armor1-1.bmp')
mainA12 = pygame.image.load('sprites/guy_armor1-2.bmp')
mainA13 = pygame.image.load('sprites/guy_armor1-3.bmp')
mainA21 = pygame.image.load('sprites/guy_armor2-1.bmp')
mainA22 = pygame.image.load('sprites/guy_armor2-2.bmp')
mainA23 = pygame.image.load('sprites/guy_armor2-3.bmp')
armourbuy1 = pygame.image.load('sprites/placeholder.bmp')
armourbuy2 = pygame.image.load('sprites/placeholder.bmp')
dirt = pygame.image.load('sprites/dirt.bmp')
grass = pygame.image.load('sprites/grass.bmp')
wood = pygame.image.load('sprites/wood.bmp')
door = pygame.image.load('sprites/door.bmp')
roof = pygame.image.load('sprites/roof.bmp')
woodfloor = pygame.image.load('sprites/wood floor.bmp')
back = pygame.image.load('sprites/background.bmp')
heartE = pygame.image.load('sprites/emptyheart.bmp')
heartH = pygame.image.load('sprites/halfheart.bmp')
heartF = pygame.image.load('sprites/fullheart.bmp')
orc1 = pygame.image.load('sprites/orcfront.bmp')
orc2 = pygame.image.load('sprites/orcfront2.bmp')
orc3 = pygame.image.load('sprites/orcback.bmp')
battle1 = pygame.image.load('sprites/battleinfo1.bmp')
battle2 = pygame.image.load('sprites/battleinfo2.bmp')
battle3 = pygame.image.load('sprites/battleinfo3.bmp')
battle4 = pygame.image.load('sprites/battleinfo4.bmp')
battle5 = pygame.image.load('sprites/battleinfo5.bmp')
battle6 = pygame.image.load('sprites/battleinfo6.bmp')
attack = pygame.image.load('sprites/attack.bmp')
defend = pygame.image.load('sprites/defend.bmp')
battleback = pygame.image.load('sprites/attackback.bmp')
counter = pygame.image.load('sprites/placeholder.bmp')
coin = pygame.image.load('sprites/coin.bmp')
M0 = pygame.image.load('sprites/0.bmp')
M1 = pygame.image.load('sprites/1.bmp')
M2 = pygame.image.load('sprites/2.bmp')
M3 = pygame.image.load('sprites/3.bmp')
M4 = pygame.image.load('sprites/4.bmp')
M5 = pygame.image.load('sprites/5.bmp')
M6 = pygame.image.load('sprites/6.bmp')
M7 = pygame.image.load('sprites/7.bmp')
M8 = pygame.image.load('sprites/8.bmp')
M9 = pygame.image.load('sprites/9.bmp')
Mback = pygame.image.load('sprites/mback.bmp')

C1 = M0
C1no = 0
C2 = M0
C2no = 0
C3 = M0
C3no = 0
C4 = M0
C4no = 0
AC1 = M5
AC1no = 5 
AC2 = M0
AC2no = 0

orc = orc2
health = 10
orchealth = 4
mainguy = main
mainguyup = 1
mainguyside = 1
WHITE = (255, 255, 255)
BLACK = (0,0,0)
play = 1
end = 0
enemy = "orc"
area = "plains"
Pattack = "attack"
Eattack = "attack"
Eattackno = 1
armourbuylvl = armourbuy1
armourbuylvlno = 1
armourlvl = 1

window = pygame.display.set_mode((0,0), FULLSCREEN)
WIDTH, HEIGHT = window.get_rect().size
#WIDTH = 1366
#HEIGHT = 768
mainX = WIDTH/3
mainY = HEIGHT/3
orcX = WIDTH/2
orcY = HEIGHT/2

background = window.copy()
background.fill(WHITE)
background.convert()



def process_events():
    global mainX
    global mainY
    global mainguy
    global mainguyup
    global mainguyside
    global area
    global health
    global Eattackno
    global Eattack
    global Pattack
    global orchealth
    global C1
    global C1no
    global C2
    global C2no
    global C3
    global C3no
    global C4
    global C4no
    global armourbuylvl
    global armourbuylvlno
    global armourlvl
    
    events = pygame.event.get()
    #process the events
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if area == "blacksmith" and mainY == 125:
                    mainY = mainY - 0
                    mainguyup = 0
                    if armourlvl == 1:
                        mainguyup = 0
                        mainguy = main4
                    if armourlvl == 2:
                        mainguyup = 0
                        mainguy = mainA13
                    if armourlvl == 3:
                        mainguyup = 0
                        mainguy = mainA23
                elif area == "blacksmith" and mainY == 125:
                    if armourlvl == 1:
                        mainY = mainY - 0
                        mainguyup = 0
                        mainguy = main4
                    if armourlvl == 2:
                        mainY = mainY - 0
                        mainguyup = 0
                        mainguy = mainA13
                    if armourlvl == 3:
                        mainY = mainY - 0
                        mainguyup = 0
                        mainguy = mainA23
                elif area == "blacksmith" and mainY > 125:
                    if armourlvl == 1:
                        mainY = mainY - 125
                        mainguyup = 0
                        mainguy = main4
                    if armourlvl == 2:
                        mainY = mainY - 125
                        mainguyup = 0
                        mainguy = mainA13
                    if armourlvl == 3:
                        mainY = mainY - 125
                        mainguyup = 0
                        mainguy = mainA23
                elif area == "battle":
                    mainX = mainX
                elif area == "shops":
                    if mainX == 1125 and mainY == 375:
                        mainY = mainY - 0
                        mainguyup = 0
                        if armourlvl == 1:
                            mainguyup = 0
                            mainguy = main4
                        if armourlvl == 2:
                            mainguyup = 0
                            mainguy = mainA13
                        if armourlvl == 3:
                            mainguyup = 0
                            mainguy = mainA23
                    elif mainX == 1250 and mainY == 375:
                        mainY = mainY - 0
                        mainguyup = 0
                        if armourlvl == 1:
                            mainguyup = 0
                            mainguy = main4
                        if armourlvl == 2:
                            mainguyup = 0
                            mainguy = mainA13
                        if armourlvl == 3:
                            mainguyup = 0
                            mainguy = mainA23
                    elif mainX == 875 and mainY == 375:
                        mainY = mainY - 0
                        mainguyup = 0
                        if armourlvl == 1:
                            mainguyup = 0
                            mainguy = main4
                        if armourlvl == 2:
                            mainguyup = 0
                            mainguy = mainA13
                        if armourlvl == 3:
                            mainguyup = 0
                            mainguy = mainA23
                    elif mainX == 750 and mainY == 375:
                        mainY = mainY - 0
                        mainguyup = 0
                        mainguy = main4
                    elif mainX == 500 and mainY == 375:
                        mainY = mainY - 0
                        mainguyup = 0
                        if armourlvl == 1:
                            mainguyup = 0
                            mainguy = main4
                        if armourlvl == 2:
                            mainguyup = 0
                            mainguy = mainA13
                        if armourlvl == 3:
                            mainguyup = 0
                            mainguy = mainA23
                    elif mainX == 375 and mainY == 375:
                        mainY = mainY - 0
                        mainguyup = 0
                        if armourlvl == 1:
                            mainguyup = 0
                            mainguy = main4
                        if armourlvl == 2:
                            mainguyup = 0
                            mainguy = mainA13
                        if armourlvl == 3:
                            mainguyup = 0
                            mainguy = mainA23
                    elif mainX == 125 and mainY == 375:
                        mainY = mainY - 0
                        mainguyup = 0
                        if armourlvl == 1:
                            mainguyup = 0
                            mainguy = main4
                        if armourlvl == 2:
                            mainguyup = 0
                            mainguy = mainA13
                        if armourlvl == 3:
                            mainguyup = 0
                            mainguy = mainA23
                    elif mainX == 0 and mainY == 375:
                        mainY = mainY - 0
                        mainguyup = 0
                        if armourlvl == 1:
                            mainguyup = 0
                            mainguy = main4
                        if armourlvl == 2:
                            mainguyup = 0
                            mainguy = mainA13
                        if armourlvl == 3:
                            mainguyup = 0
                            mainguy = mainA23
                    elif mainX == 250 and mainY == 375:
                        area = "blacksmith"
                        mainX = 625
                        mainY = 500
                    elif mainY > 0:
                        if armourlvl == 1:
                            mainY = mainY - 125
                            mainguyup = 0
                            mainguy = main4
                        if armourlvl == 2:
                            mainY = mainY - 125
                            mainguyup = 0
                            mainguy = mainA13
                        if armourlvl == 3:
                            mainY = mainY - 125
                            mainguyup = 0
                            mainguy = mainA23
                elif mainY == 0:
                    if area == "plains":
                        area = "shops"
                        mainY = 625
                elif mainY > 0:
                    mainguyup = 0
                    if armourlvl == 1:
                        mainY = mainY - 125
                        mainguyup = 0
                        mainguy = main4
                    if armourlvl == 2:
                        mainY = mainY - 125
                        mainguyup = 0
                        mainguy = mainA13
                    if armourlvl == 3:
                        mainY = mainY - 125
                        mainguyup = 0
                        mainguy = mainA23
            elif event.key == K_DOWN:
                if area == "blacksmith" and mainY == 500:
                    if mainX ==625:
                        area = "shops"
                        mainX = 250
                        mainY = 375
                    mainY = mainY+0
                    mainguyup = 1
                    if mainguyside == 1:
                        if armourlvl == 1:
                            mainguy = main
                        if armourlvl == 2:
                            mainguy = mainA11
                        if armourlvl == 3:
                            mainuy = mainA21
                    elif mainguyside == 0:
                        if armourlvl == 1:
                            mainguy = main2
                        if armourlvl == 2:
                            mainguy = mainA12
                        if armourlvl == 3:
                            mainuy = mainA22
                elif mainY < 625:
                    mainY = mainY + 125
                    mainguyup = 1
                    if mainguyside == 1:
                        if armourlvl == 1:
                            mainguy = main
                        if armourlvl == 2:
                            mainguy = mainA11
                        if armourlvl == 3:
                            mainguy = mainA21
                    elif mainguyside == 0:
                        if armourlvl == 1:
                            mainguy = main2
                        if armourlvl == 2:
                            mainguy = mainA12
                        if armourlvl == 3:
                            mainguy = mainA22
                elif area == "battle":
                    mainX = mainX
                elif mainY == 625:
                        if area == "shops":
                            area = "plains"
                            mainY = 0
                            if mainguyside == 1:
                                if armourlvl == 1:
                                    mainguy = main
                                if armourlvl == 2:
                                    mainguy = mainA11
                                if armourlvl == 3:
                                    mainuy = mainA21
                            elif mainguyside == 0:
                                if armourlvl == 1:
                                    mainguy = main2
                                if armourlvl == 2:
                                    mainguy = mainA12
                                if armourlvl == 3:
                                   mainguy = mainA22
            elif event.key == K_RIGHT:
                if area == "blacksmith" and mainX == 1125:
                    mainX = mainX-0
                    mainguyside = 0
                    if armourlvl == 1:
                            mainguy = main2
                    if armourlvl == 2:
                        mainguy = mainA12
                    if armourlvl == 3:
                        mainguy = mainA22
                elif area == "battle":
                    mainX = mainX
                elif area == "shops":
                    if mainX == 625 and mainY == 125:
                        mainX = mainX + 0
                        mainguyside = 0
                        if armourlvl == 1:
                            mainguy = main2
                        if armourlvl == 2:
                            mainguy = mainA12
                        if armourlvl == 3:
                            mainguy = mainA22
                    elif mainX == 625 and mainY == 250:
                        mainX = mainX + 0
                        mainguyside = 0
                        if armourlvl == 1:
                            mainguy = main2
                        if armourlvl == 2:
                            mainguy = mainA12
                        if armourlvl == 3:
                            mainguy = mainA22
                    elif mainX == 625 and mainY == 0:
                        mainX = mainX + 0
                        mainguyside = 0
                        if armourlvl == 1:
                            mainguy = main2
                        if armourlvl == 2:
                            mainguy = mainA12
                        if armourlvl == 3:
                            mainguy = mainA22
                    elif mainX < 1250:
                        mainX = mainX + 125
                        mainguyside = 0
                        if armourlvl == 1:
                            mainguy = main2
                        if armourlvl == 2:
                            mainguy = mainA12
                        if armourlvl == 3:
                            mainguy = mainA22
                elif mainX < 1250:
                    mainX = mainX + 125
                    mainguyside = 0
                    if armourlvl == 1:
                        mainguy = main2
                    if armourlvl == 2:
                        mainguy = mainA12
                    if armourlvl == 3:
                        mainguy = mainA22
            elif event.key == K_LEFT:
                if area == "blacksmith" and mainX == 500:
                    mainX = mainX-0
                    mainguyside = 0
                    if armourlvl == 1:
                        mainguy = main
                    if armourlvl == 2:
                        mainguy = mainA11
                    if armourlvl == 3:
                        mainguy = mainA21
                elif area == "battle":
                    mainX = mainX
                elif area == "shops":
                    if mainX == 625 and mainY == 125:
                        mainX = mainX - 0
                        mainguyside = 0
                        if armourlvl == 1:
                            mainguy = main
                        if armourlvl == 2:
                            mainguy = mainA11
                        if armourlvl == 3:
                            mainguy = mainA21
                    elif mainX == 625 and mainY == 250:
                        mainX = mainX - 0
                        mainguyside = 0
                        if armourlvl == 1:
                            mainguy = main
                        if armourlvl == 2:
                            mainguy = mainA11
                        if armourlvl == 3:
                            mainguy = mainA21
                    elif mainX == 625 and mainY == 0:
                        mainX = mainX - 0
                        mainguyside = 0
                        if armourlvl == 1:
                            mainguy = main
                        if armourlvl == 2:
                            mainguy = mainA11
                        if armourlvl == 3:
                            mainguy = mainA21
                    elif mainX > 0:
                        mainX = mainX - 125
                        mainguyside = 0
                        if armourlvl == 1:
                            mainguy = main
                        if armourlvl == 2:
                            mainguy = mainA11
                        if armourlvl == 3:
                            mainguy = mainA21
                elif mainX > 0:
                    mainX = mainX - 125
                    mainguyside = 1
                    if armourlvl == 1:
                        mainguy = main
                    if armourlvl == 2:
                        mainguy = mainA11
                    if armourlvl == 3:
                        mainguy = mainA21
            elif event.key == K_a:
                health = health -1
                if health == -1:
                    health = 10
            elif event.key == K_s:
                area = "plains"
            elif event.key == K_f:
                if area == "battle":
                    Pattack = "attack"
                    Eattackno = (randint(1,3))
                    if Eattackno == 1:
                        Eattack = "attack"
                    elif Eattackno == 2:
                        Eattack = "block"
                    elif Eattackno == 3:
                        Eattack = "nothing"
                    if Eattack == "block" and Pattack == "attack":
                        orchealth = orchealth
                    elif Pattack == "attack":
                        orchealth = orchealth - 1
                        if orchealth < 1:
                            C1no = C1no + 25
                            area = "plains"
                            orchealth = 4
                    if Eattack == "attack":
                        health = health - (4 - armourlvl)
                        
                    print(orchealth)
            elif event.key == K_d:
                if area == "battle":
                    Pattack = "block"
                    Eattackno = (randint(1,3))
                    if Eattackno == 1:
                        Eattack = "attack"
                    elif Eattackno == 2:
                        Eattack = "block"
                    elif Eattackno == 3:
                        Eattack = "nothing"
                    if Pattack == "block" and Eattack == "attack":
                        health = health
            elif event.key == K_b:
                if area == "blacksmith":
                    if mainX == 625 and mainY == 250:
                        if armourbuylvlno == 1:
                            if C2no > 0:
                                C1no = C1no - AC1no
                                armourbuylvlno = 2
                                armourlvl = 2
                            elif C1no > AC1no-1:
                                C1no = C1no - AC1no
                                armourbuylvlno = 2
                                armourlvl = 2
                        elif armourbuylvlno == 2:
                            if C3no > 0:
                                C1no = C1no - AC1no
                                C2no = C2no - AC2no
                                armourbuylvlno = 3
                                armourbuylvl = woodfloor
                                armourlvl = 3
                            elif C2no > AC2no-1 and C1no > AC1no-1:
                                C2no = C2no - AC2no
                                C1no = C1no - AC1no
                                armourbuylvlno = 3
                                armourbuylvl = woodfloor
                                armourlvl = 3
                            elif C2no > AC2no:
                                C2no = C2no - AC2no
                                C1no = C1no - AC1no
                                armourbuylvlno = 3
                                armourbuylvl = woodfloor
                                armourlvl = 3
            elif event.key == K_v:
                armourbuylvlno = 1
                armourlvl = 1
            elif event.key == K_q:
                C1no = C1no + 1
            elif event.key == K_w:
                C1no = C1no - 1
            elif event.key == K_e:
                C1no = C1no + 5
            elif event.key == K_r:
                C1no = C1no - 5
                print(Eattack)
                print(Pattack)
                print(Eattackno)
            elif event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
        elif event.type == QUIT:
            pygame.quit()          



class Surf(pygame.Surface):
    def __init__(self, rect):
        self.rect = rect
        pygame.Surface.__init__(self, (self.rect.width, self.rect.height))
    def get_rect(self, **kwargs):
        trect = self.rect
        for k in kwargs:
            self.rect.__dict__[k] = kwargs[k]
        return self.rect
    def get_simple_rect(self, **kwargs):
        return pygame.Surface.get_rect(self, **kwargs)

while play > end:
    WIDTH, HEIGHT = window.get_rect().size
    window.blit(background, (0,0))
    heal = (randint(0,1000))
    if heal == 7 and health < 10 and health > 0:
        health = health + 1
    if C1no > 9:
        C2no = C2no + 1
        C1no = C1no - 10
    if C3no > 0 or C2no > 0 or C4no > 0:
        if C1no < 0:
            C2no = C2no - 1
            C1no = 10 + C1no
    elif C1no < 0:
        C1no = 0
    if C2no > 9:
        C3no = C3no + 1
        C2no = C2no - 10
    if C4no > 0 or C3no > 0:
        if C2no < 0:
            C3no = C3no - 1
            C2no = 10 + C2no
    elif C2no < 0:
        C2no = 0
    if C3no > 9:
        C4no = C4no + 1
        C3no = C3no - 10
    if C3no < 0 and C4no > 0:
        C4no = C4no - 1
        C3no = 10 + C3no
    elif C3no < 0:
        C3no = 0
    if C1no == 0:
        C1 = M0
    elif C1no == 1:
        C1 = M1
    elif C1no == 2:
        C1 = M2
    elif C1no == 3:
        C1 = M3
    elif C1no == 4:
        C1 = M4
    elif C1no == 5:
        C1 = M5
    elif C1no == 6:
        C1 = M6
    elif C1no == 7:
        C1 = M7
    elif C1no == 8:
        C1 = M8
    elif C1no == 9:
        C1 = M9
    if C2no == 0:
        C2 = M0
    elif C2no == 1:
        C2 = M1
    elif C2no == 2:
        C2 = M2
    elif C2no == 3:
        C2 = M3
    elif C2no == 4:
        C2 = M4
    elif C2no == 5:
        C2 = M5
    elif C2no == 6:
        C2 = M6
    elif C2no == 7:
        C2 = M7
    elif C2no == 8:
        C2 = M8
    elif C2no == 9:
        C2 = M9
    if C3no == 0:
        C3 = M0
    elif C3no == 1:
        C3 = M1
    elif C3no == 2:
        C3 = M2
    elif C3no == 3:
        C3 = M3
    elif C3no == 4:
        C3 = M4
    elif C3no == 5:
        C3 = M5
    elif C3no == 6:
        C3 = M6
    elif C3no == 7:
        C3 = M7
    elif C3no == 8:
        C3 = M8
    elif C3no == 9:
        C3 = M9
    if C4no == 0:
        C4 = M0
    elif C4no == 1:
        C4 = M1
    elif C4no == 2:
        C4 = M2
    elif C4no == 3:
        C4 = M3
    elif C4no == 4:
        C4 = M4
    elif C4no == 5:
        C4 = M5
    elif C4no == 6:
        C4 = M6
    elif C4no == 7:
        C4 = M7
    elif C4no == 8:
        C4 = M8
    elif C4no == 9:
        C4 = M9
    if area == "plains":
        window.blit(grass, (0,0))
        window.blit(grass, (125,0))
        window.blit(dirt, (250,0))
        window.blit(grass, (375,0))
        window.blit(grass, (500,0))
        window.blit(grass, (625,0))
        window.blit(grass, (750,0))
        window.blit(grass, (875,0))
        window.blit(dirt, (1000,0))
        window.blit(grass, (1125,0))
        window.blit(grass, (1250,0))
        window.blit(grass, (0,125))
        window.blit(grass, (125,125))
        window.blit(dirt, (250,125))
        window.blit(grass, (375,125))
        window.blit(grass, (500,125))
        window.blit(grass, (625,125))
        window.blit(grass, (750,125))
        window.blit(grass, (875,125))
        window.blit(dirt, (1000,125))
        window.blit(grass, (1125,125))
        window.blit(grass, (1250,125))
        window.blit(dirt, (0,250))
        window.blit(dirt, (125,250))
        window.blit(dirt, (250,250))
        window.blit(dirt, (375,250))
        window.blit(dirt, (500,250))
        window.blit(dirt, (625,250))
        window.blit(dirt, (750,250))
        window.blit(dirt, (875,250))
        window.blit(dirt, (1000,250))
        window.blit(dirt, (1125,250))
        window.blit(dirt, (1250,250))
        window.blit(grass, (0,375))
        window.blit(grass, (125,375))
        window.blit(grass, (250,375))
        window.blit(grass, (375,375))
        window.blit(dirt, (500,375))
        window.blit(grass, (625,375))
        window.blit(grass, (750,375))
        window.blit(grass, (875,375))
        window.blit(grass, (1000,375))
        window.blit(grass, (1125,375))
        window.blit(grass, (1250,375))
        window.blit(grass, (0,500))
        window.blit(grass, (125,500))
        window.blit(grass, (250,500))
        window.blit(grass, (375,500))
        window.blit(dirt, (500,500))
        window.blit(grass, (625,500))
        window.blit(grass, (750,500))
        window.blit(grass, (875,500))
        window.blit(grass, (1000,500))
        window.blit(grass, (1125,500))
        window.blit(grass, (1250,500))
        window.blit(grass, (0,625))
        window.blit(grass, (125,625))
        window.blit(grass, (250,625))
        window.blit(grass, (375,625))
        window.blit(dirt, (500,625))
        window.blit(grass, (625,625))
        window.blit(grass, (750,625))
        window.blit(grass, (875,625))
        window.blit(grass, (1000,625))
        window.blit(grass, (1125,625))
        window.blit(grass, (1250,625))
        window.blit(grass, (0,750))
        window.blit(grass, (125,750))
        window.blit(grass, (250,750))
        window.blit(grass, (375,750))
        window.blit(dirt, (500,750))
        window.blit(grass, (625,750))
        window.blit(grass, (750,750))
        window.blit(grass, (875,750))
        window.blit(grass, (1000,750))
        window.blit(grass, (1125,750))
        window.blit(grass, (1250,750))
        window.blit(orc, (orcX,orcY))
    if area == "shops":
        window.blit(grass, (0,750))
        window.blit(grass, (125,750))
        window.blit(dirt, (250,750))
        window.blit(grass, (375,750))
        window.blit(grass, (500,750))
        window.blit(grass, (625,750))
        window.blit(grass, (750,750))
        window.blit(grass, (875,750))
        window.blit(dirt, (1000,750))
        window.blit(grass, (1125,750))
        window.blit(grass, (1250,750))
        window.blit(grass, (0,625))
        window.blit(grass, (125,625))
        window.blit(dirt, (250,625))
        window.blit(grass, (375,625))
        window.blit(grass, (500,625))
        window.blit(grass, (625,625))
        window.blit(grass, (750,625))
        window.blit(grass, (875,625))
        window.blit(dirt, (1000,625))
        window.blit(grass, (1125,625))
        window.blit(grass, (1250,625))
        window.blit(grass, (0,500))
        window.blit(grass, (125,500))
        window.blit(dirt, (250,500))
        window.blit(dirt, (375,500))
        window.blit(dirt, (500,500))
        window.blit(dirt, (625,500))
        window.blit(dirt, (750,500))
        window.blit(dirt, (875,500))
        window.blit(dirt, (1000,500))
        window.blit(grass, (1125,500))
        window.blit(grass, (1250,500))
        window.blit(grass, (0,375))
        window.blit(grass, (125,375))
        window.blit(dirt, (250,375))
        window.blit(grass, (375,375))
        window.blit(grass, (500,375))
        window.blit(grass, (625,375))
        window.blit(grass, (750,375))
        window.blit(grass, (875,375))
        window.blit(dirt, (1000,375))
        window.blit(grass, (1125,375))
        window.blit(grass, (1250,375))
        window.blit(wood, (0,250))
        window.blit(wood, (125,250))
        window.blit(door, (250,250))
        window.blit(wood, (375,250))
        window.blit(wood, (500,250))
        window.blit(grass, (625,250))
        window.blit(wood, (750,250))
        window.blit(wood, (875,250))
        window.blit(door, (1000,250))
        window.blit(wood, (1125,250))
        window.blit(wood, (1250,250))
        window.blit(wood, (0,125))
        window.blit(wood, (125,125))
        window.blit(wood, (250,125))
        window.blit(wood, (375,125))
        window.blit(wood, (500,125))
        window.blit(grass, (625,125))
        window.blit(wood, (750,125))
        window.blit(wood, (875,125))
        window.blit(wood, (1000,125))
        window.blit(wood, (1125,125))
        window.blit(wood, (1250,125))
        window.blit(roof, (0,0))
        window.blit(roof, (125,0))
        window.blit(roof, (250,0))
        window.blit(roof, (375,0))
        window.blit(roof, (500,0))
        window.blit(grass, (625,0))
        window.blit(roof, (750,0))
        window.blit(roof, (875,0))
        window.blit(roof, (1000,0))
        window.blit(roof, (1125,0))
        window.blit(roof, (1250,0))
    elif area == "blacksmith":
        window.blit(back, (0,0))
        window.blit(back, (125,0))
        window.blit(back, (250,0))
        window.blit(back, (375,0))
        window.blit(back, (500,0))
        window.blit(back, (625,0))
        window.blit(back, (750,0))
        window.blit(back, (875,0))
        window.blit(back, (1000,0))
        window.blit(back, (1125,0))
        window.blit(back, (1250,0))
        window.blit(back, (0,125))
        window.blit(woodfloor, (125,125))
        window.blit(woodfloor, (250,125))
        window.blit(counter, (375,125))
        window.blit(woodfloor, (500,125))
        window.blit(woodfloor, (625,125))
        window.blit(woodfloor, (750,125))
        window.blit(woodfloor, (875,125))
        window.blit(woodfloor, (1000,125))
        window.blit(woodfloor, (1125,125))
        window.blit(back, (1250,125))
        window.blit(back, (0,250))
        window.blit(woodfloor, (125,250))
        window.blit(woodfloor, (250,250))
        window.blit(counter, (375,250))
        window.blit(woodfloor, (500,250))
        window.blit(woodfloor, (625,250))
        window.blit(woodfloor, (750,250))
        window.blit(woodfloor, (875,250))
        window.blit(woodfloor, (1000,250))
        window.blit(woodfloor, (1125,250))
        window.blit(back, (1250,250))
        window.blit(back, (0,375))
        window.blit(woodfloor, (125,375))
        window.blit(woodfloor, (250,375))
        window.blit(counter, (375,375))
        window.blit(woodfloor, (500,375))
        window.blit(woodfloor, (625,375))
        window.blit(woodfloor, (750,375))
        window.blit(woodfloor, (875,375))
        window.blit(woodfloor, (1000,375))
        window.blit(woodfloor, (1125,375))
        window.blit(back, (1250,375))
        window.blit(back, (0,500))
        window.blit(woodfloor, (125,500))
        window.blit(woodfloor, (250,500))
        window.blit(counter, (375,500))
        window.blit(woodfloor, (500,500))
        window.blit(woodfloor, (625,500))
        window.blit(woodfloor, (750,500))
        window.blit(woodfloor, (875,500))
        window.blit(woodfloor, (1000,500))
        window.blit(woodfloor, (1125,500))
        window.blit(back, (1250,500))
        window.blit(back, (0,625))
        window.blit(wood, (125,625))
        window.blit(wood, (250,625))
        window.blit(wood, (375,625))
        window.blit(wood, (500,625))
        window.blit(door, (625,625))
        window.blit(wood, (750,625))
        window.blit(wood, (875,625))
        window.blit(wood, (1000,625))
        window.blit(wood, (1125,625))
        window.blit(back, (1250,625))
        window.blit(back, (0,750))
        window.blit(back, (125,750))
        window.blit(back, (250,750))
        window.blit(back, (375,750))
        window.blit(back, (500,750))
        window.blit(back, (625,750))
        window.blit(back, (750,750))
        window.blit(back, (875,750))
        window.blit(back, (1000,750))
        window.blit(back, (1125,750))
        window.blit(back, (1250,750))
        if armourbuylvlno < 4:
            window.blit(armourbuylvl, (625,125))
            window.blit(coin, (590,200))
            window.blit(Mback, (675,200))
            window.blit(Mback, (710,200))
            window.blit(AC2, (680,200))
            window.blit(AC1, (715,200))
        if armourbuylvlno == 1:
            armourbuylvl = armourbuy1
            AC2 = M0
            AC1 = M5
            AC2no = 0
            AC1no = 5
        elif armourbuylvlno == 2:
            armourbuylvl = armourbuy2
            AC2 = M1
            AC1 = M5
            AC2no = 1
            AC1no = 5
    elif area == "battle":
        if armourlvl == 1:
            mainguy = main2
        if armourlvl == 2:
            mainguy = mainA12
        if armourlvl == 3:
            mainguy = mainA22
        window.blit(back, (0,750))
        window.blit(back, (125,750))
        window.blit(back, (250,750))
        window.blit(back, (375,750))
        window.blit(back, (500,750))
        window.blit(back, (625,750))
        window.blit(back, (750,750))
        window.blit(back, (875,750))
        window.blit(back, (1000,750))
        window.blit(back, (1125,750))
        window.blit(back, (1250,750))
        window.blit(back, (0,625))
        window.blit(back, (125,625))
        window.blit(back, (250,625))
        window.blit(back, (375,625))
        window.blit(battle4, (500,625))
        window.blit(battle5, (625,625))
        window.blit(battle6, (750,625))
        window.blit(back, (875,625))
        window.blit(back, (1000,625))
        window.blit(back, (1125,625))
        window.blit(back, (1250,625))
        window.blit(back, (0,500))
        window.blit(back, (125,500))
        window.blit(back, (250,500))
        window.blit(back, (375,500))
        window.blit(battle1, (500,500))
        window.blit(battle2, (625,500))
        window.blit(battle3, (750,500))
        window.blit(back, (875,500))
        window.blit(back, (1000,500))
        window.blit(back, (1125,500))
        window.blit(back, (1250,500))
        window.blit(back, (0,375))        
        window.blit(back, (125,375))
        window.blit(grass, (250,375))
        window.blit(grass, (375,375))
        window.blit(grass, (500,375))
        window.blit(grass, (625,375))
        window.blit(grass, (750,375))
        window.blit(grass, (875,375))
        window.blit(grass, (1000,375))
        window.blit(back, (1125,375))
        window.blit(back, (1250,375))
        window.blit(back, (0,250))
        window.blit(battleback, (125,250))
        window.blit(grass, (250,250))
        window.blit(grass, (375,250))
        window.blit(grass, (500,250))
        window.blit(grass, (625,250))
        window.blit(grass, (750,250))
        window.blit(grass, (875,250))
        window.blit(grass, (1000,250))
        window.blit(battleback, (1125,250))
        window.blit(back, (1250,250))
        window.blit(back, (0,125))
        window.blit(back, (125,125))
        window.blit(grass, (250,125))
        window.blit(grass, (375,125))
        window.blit(grass, (500,125))
        window.blit(grass, (625,125))
        window.blit(grass, (750,125))
        window.blit(grass, (875,125))
        window.blit(grass, (1000,125))
        window.blit(back, (1125,125))
        window.blit(back, (1250,125))
        window.blit(back, (0,0))
        window.blit(back, (125,0))
        window.blit(back, (250,0))
        window.blit(back, (375,0))
        window.blit(back, (500,0))
        window.blit(back, (625,0))
        window.blit(back, (750,0))
        window.blit(back, (875,0))
        window.blit(back, (1000,0))
        window.blit(back, (1125,0))
        window.blit(back, (1250,0))
        if Pattack == "attack":
            window.blit(attack, (125,250))
        elif Pattack == "block":
            window.blit(defend, (125,250))
        if Eattack == "attack":
            window.blit(attack, (1125,250))
        elif Eattack == "block":
            window.blit(defend, (1125,250))
        mainX = 250
        mainY = 250
        orc = orc1
        orcX = 1000
        orcY = 250
        window.blit(orc, (orcX,orcY))
        if orchealth == 0:
            window.blit(heartE, (1250,0))
            window.blit(heartE, (1200,0))
        if orchealth == 1:
            window.blit(heartH, (1250,0))
            window.blit(heartE, (1200,0))
            
        if orchealth == 2:
            window.blit(heartF, (1250,0))
            window.blit(heartE, (1200,0))
        if orchealth == 3:
            window.blit(heartF, (1250,0))
            window.blit(heartH, (1200,0))
        if orchealth == 4:
            window.blit(heartF, (1250,0))
            window.blit(heartF, (1200,0))
    
    if health == 0:
        window.blit(heartE, (0,0))
        window.blit(heartE, (50,0))
        window.blit(heartE, (100,0))
        window.blit(heartE, (150,0))
        window.blit(heartE, (200,0))
    if health == 1:
        window.blit(heartH, (0,0))
        window.blit(heartE, (50,0))
        window.blit(heartE, (100,0))
        window.blit(heartE, (150,0))
        window.blit(heartE, (200,0))
    if health == 2:
        window.blit(heartF, (0,0))
        window.blit(heartE, (50,0))
        window.blit(heartE, (100,0))
        window.blit(heartE, (150,0))
        window.blit(heartE, (200,0))
    if health == 3:
        window.blit(heartF, (0,0))
        window.blit(heartH, (50,0))
        window.blit(heartE, (100,0))
        window.blit(heartE, (150,0))
        window.blit(heartE, (200,0))
    if health == 4:
        window.blit(heartF, (0,0))
        window.blit(heartF, (50,0))
        window.blit(heartE, (100,0))
        window.blit(heartE, (150,0))
        window.blit(heartE, (200,0))
    if health == 5:
        window.blit(heartF, (0,0))
        window.blit(heartF, (50,0))
        window.blit(heartH, (100,0))
        window.blit(heartE, (150,0))
        window.blit(heartE, (200,0))
    if health == 6:
        window.blit(heartF, (0,0))
        window.blit(heartF, (50,0))
        window.blit(heartF, (100,0))
        window.blit(heartE, (150,0))
        window.blit(heartE, (200,0))
    if health == 7:
        window.blit(heartF, (0,0))
        window.blit(heartF, (50,0))
        window.blit(heartF, (100,0))
        window.blit(heartH, (150,0))
        window.blit(heartE, (200,0))
    if health == 8:
        window.blit(heartF, (0,0))
        window.blit(heartF, (50,0))
        window.blit(heartF, (100,0))
        window.blit(heartF, (150,0))
        window.blit(heartE, (200,0))
    if health == 9:
        window.blit(heartF, (0,0))
        window.blit(heartF, (50,0))
        window.blit(heartF, (100,0))
        window.blit(heartF, (150,0))
        window.blit(heartH, (200,0))
    if health == 10:
        window.blit(heartF, (0,0))
        window.blit(heartF, (50,0))
        window.blit(heartF, (100,0))
        window.blit(heartF, (150,0))
        window.blit(heartF, (200,0))
    if area == "plains" or area == "shops" or area == "blacksmith":
        window.blit(coin, (1100,0))
        window.blit(Mback, (1200,0))
        window.blit(Mback, (1235,0))
        window.blit(Mback, (1270,0))
        window.blit(Mback, (1305,0))
        window.blit(C1, (1310,0))
        window.blit(C2, (1275,0))
        window.blit(C3, (1240,0))
        window.blit(C4, (1205,0))
            
    orcmove = (randint(0,15))
    if area == "plains":
        if orcX == 1000 and orcY == 250:
            orcX = 750
            orcY = 500
        if orcmove == 3:
            if orcX == 750 and orcY == 500:
                orcX = 875
                orcY = 500
                orc = orc2
            elif orcX == 875 and orcY == 500:
                orcX = 1000
                orcY = 500
                orc = orc2
            elif orcX == 1000 and orcY == 500:
                orcX = 1000
                orcY = 625
                orc = orc1
            elif orcX == 1000 and orcY == 625:
                orcX = 875
                orcY = 625
                orc = orc1
            elif orcX == 875 and orcY == 625:
                orcX = 750
                orcY = 625
                orc = orc1
            elif orcX == 750 and orcY == 625:
                orcX = 750
                orcY = 500
                orc = orc3
        if mainX == orcX and mainY == orcY :
            area = "battle"
            enemy = "orc"
    window.blit(mainguy, (mainX,mainY))
    if health < 1:
        area = "death"
        window.blit(back, (0,0))
        window.blit(back, (125,0))
        window.blit(back, (250,0))
        window.blit(back, (375,0))
        window.blit(back, (500,0))
        window.blit(back, (625,0))
        window.blit(back, (750,0))
        window.blit(back, (875,0))
        window.blit(back, (1000,0))
        window.blit(back, (1125,0))
        window.blit(back, (1250,0))
        window.blit(back, (0,125))
        window.blit(back, (125,125))
        window.blit(back, (250,125))
        window.blit(back, (375,125))
        window.blit(back, (500,125))
        window.blit(back, (625,125))
        window.blit(back, (750,125))
        window.blit(back, (875,125))
        window.blit(back, (1000,125))
        window.blit(back, (1125,125))
        window.blit(back, (1250,125))
        window.blit(back, (0,250))
        window.blit(back, (125,250))
        window.blit(back, (250,250))
        window.blit(back, (375,250))
        window.blit(back, (500,250))
        window.blit(back, (625,250))
        window.blit(back, (750,250))
        window.blit(back, (875,250))
        window.blit(back, (1000,250))
        window.blit(back, (1125,250))
        window.blit(back, (1250,250))
        window.blit(back, (0,375))
        window.blit(back, (125,375))
        window.blit(back, (250,375))
        window.blit(back, (375,375))
        window.blit(back, (500,375))
        window.blit(back, (625,375))
        window.blit(back, (750,375))
        window.blit(back, (875,375))
        window.blit(back, (1000,375))
        window.blit(back, (1125,375))
        window.blit(back, (1250,375))
        window.blit(back, (0,500))
        window.blit(back, (125,500))
        window.blit(back, (250,500))
        window.blit(back, (375,500))
        window.blit(back, (500,500))
        window.blit(back, (625,500))
        window.blit(back, (750,500))
        window.blit(back, (875,500))
        window.blit(back, (1000,500))
        window.blit(back, (1125,500))
        window.blit(back, (1250,500))
        window.blit(back, (0,625))
        window.blit(back, (125,625))
        window.blit(back, (250,625))
        window.blit(back, (375,625))
        window.blit(back, (500,625))
        window.blit(back, (625,625))
        window.blit(back, (750,625))
        window.blit(back, (875,625))
        window.blit(back, (1000,625))
        window.blit(back, (1125,625))
        window.blit(back, (1250,625))
        window.blit(back, (0,750))
        window.blit(back, (125,750))
        window.blit(back, (250,750))
        window.blit(back, (375,750))
        window.blit(back, (500,750))
        window.blit(back, (625,750))
        window.blit(back, (750,750))
        window.blit(back, (875,750))
        window.blit(back, (1000,750))
        window.blit(back, (1125,750))
        window.blit(back, (1250,750))
        
    
    process_events()
    pygame.display.update()
pygame.quit()
    
