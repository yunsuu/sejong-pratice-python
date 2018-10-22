#event key == ord('문자')


import pygame, sys, time
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1000
WINDOWHEIGHT = 700
BUTTONWIDTH = 60
BUTTONHEIGHT = 15
BUTTONGAP = 10
BOXWIDTH = 970
BOXHEIGHT = 200
BOX_X = 15
BOX_Y = 485
BOXGAP = 15

SCENE_NUM = 1

#COLOR (R,G,B)
DARKGRAY = (40,40,40)

#TEXT
TEXT = pygame.image.load('시작화면.jpg')

#PEOPLE
PEOPLE = pygame.image.load('교수님1.jpg')
#BUTTON1
BUTTON1RECT_X = int(WINDOWWIDTH - BUTTONWIDTH*2 - BUTTONGAP*2 - BOXGAP)
BUTTON1RECT_Y = int(WINDOWHEIGHT - BOXGAP - BOXHEIGHT)
BUTTON1RECT = pygame.Rect(BUTTON1RECT_X,BUTTON1RECT_Y,BUTTONWIDTH,BUTTONHEIGHT)
#BUTTON2
BUTTON2RECT_X = int(WINDOWWIDTH - BUTTONWIDTH - BUTTONGAP - BOXGAP)
BUTTON2RECT_Y = int(WINDOWHEIGHT - BOXGAP - BOXHEIGHT)
BUTTON2RECT = pygame.Rect(BUTTON2RECT_X,BUTTON2RECT_Y,BUTTONWIDTH,BUTTONHEIGHT)
#BOX
BOXRECT = pygame.Rect(BOX_X,BOX_Y,BOXWIDTH,BOXHEIGHT)
#BACKGROUND 설정
BACKGROUND= pygame.image.load('세종대학교.jpg')
#졸림 사진
HAPPY = pygame.image.load('건강.jpg')
HAPPY = pygame.transform.scale(HAPPY, (400,400))
SAD = pygame.image.load('안건강.jpg')
SAD = pygame.transform.scale(SAD, (400,400))
GRADE = 4
HEALTH = 3





global FPSCLOCK, DISPLAYSURF, BASICFONT
 
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) #윈도우창 크기 설정
pygame.display.set_caption('학점 시뮬레이션') #윈도우창 이름 설정
BASICFONT = pygame.font.Font('freesansbold.ttf',25)
FINISH = False
while not FINISH: #game loop
           
    for event in pygame.event.get():
        GRADE_TEXT = BASICFONT.render("GRADE: %d" %(GRADE), True, (40,40,40))
        HEALTH_TEXT = BASICFONT.render("HEALTH: %d" %(HEALTH), True, (40,40,40))
        if HEALTH == 0:
            DISPLAYSURF.fill((255,255,255))
            TEXT=pygame.image.load('게임오버건강.png')
            BACKGROUND = pygame.image.load('게임오버배경.jpg')
            BACKGROUND = pygame.transform.scale(BACKGROUND, (1000,700))
            DISPLAYSURF.blit(BACKGROUND, (0,0))
            DISPLAYSURF.blit(TEXT,(BOXGAP+10,WINDOWHEIGHT-BOXGAP - BOXHEIGHT + 10))
            break
        if GRADE == 0:
            DISPLAYSURF.fill((255,255,255))
            TEXT=pygame.image.load('게임오버학점.png')
            BACKGROUND = pygame.image.load('게임오버배경.jpg')
            BACKGROUND = pygame.transform.scale(BACKGROUND, (1000,700))
            DISPLAYSURF.blit(BACKGROUND, (0,0))
            DISPLAYSURF.blit(TEXT,(BOXGAP+10,WINDOWHEIGHT-BOXGAP - BOXHEIGHT + 10))
            break
        if SCENE_NUM == 1 or SCENE_NUM==2 or SCENE_NUM==3 or SCENE_NUM == 8 or SCENE_NUM == 13 or SCENE_NUM == 14 or SCENE_NUM == 17:
            DISPLAYSURF.fill((255,255,255))
            BACKGROUND = pygame.transform.scale(BACKGROUND,(1000,700))
            DISPLAYSURF.blit(BACKGROUND, (0,0))
            DISPLAYSURF.blit(TEXT,(BOXGAP+10,WINDOWHEIGHT-BOXGAP - BOXHEIGHT + 10))
            DISPLAYSURF.blit(GRADE_TEXT,(0,100))
            DISPLAYSURF.blit(HEALTH_TEXT,(0,130))
        else:
            DISPLAYSURF.fill((255,255,255))
            BACKGROUND = pygame.transform.scale(BACKGROUND,(1000,700))
            DISPLAYSURF.blit(BACKGROUND,(0,0))
            DISPLAYSURF.blit(TEXT,(BOXGAP+50,WINDOWHEIGHT-BOXGAP - BOXHEIGHT + 10))
            PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
            DISPLAYSURF.blit(PEOPLE,(BOXGAP+300,WINDOWHEIGHT - BOXGAP - BOXHEIGHT-500))
            DISPLAYSURF.blit(GRADE_TEXT,(0,100))
            DISPLAYSURF.blit(HEALTH_TEXT,(0,130))
        if event.type == pygame.KEYDOWN:
            if SCENE_NUM==1:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면1.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM==2:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면2.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM==3:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면3.jpg')
                    BACKGROUND = pygame.image.load('강의실.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 4:
                if event.key == pygame.K_SPACE:
                    TEXT = pygame.image.load('장면4.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 5:
                if event.key == pygame.K_SPACE:
                    TEXT = pygame.image.load('장면5.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM==6:
                if event.key == ord('1'):
                    TEXT=pygame.image.load('장면5-1.jpg')
                    PEOPLE = pygame.image.load('교수님2.jpg')
                    PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
                    GRADE = GRADE - 1
                    SCENE_NUM = SCENE_NUM + 1
                    continue
                elif event.key == ord('2'):
                    TEXT=pygame.image.load('장면5-2.jpg')
                    PEOPLE = pygame.image.load('건강.jpg')
                    PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
                    HEALTH = HEALTH + 1
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 7:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면6.jpg')
                    BACKGROUND=pygame.image.load('세종대학교.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 8:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면7.jpg')
                    PEOPLE = pygame.image.load('친구.jpg')
                    PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 9:
                if event.key == pygame.K_SPACE:
                    TEXT = pygame.image.load('장면8.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 10:
                if event.key == pygame.K_SPACE:
                    TEXT = pygame.image.load('장면9.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM==11:
                 if event.key == ord('1'):
                    TEXT=pygame.image.load('장면9-1.png')
                    PEOPLE = pygame.image.load('친구불쾌.jpg')
                    PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
                    HEALTH = HEALTH - 1
                    SCENE_NUM = SCENE_NUM + 1
                    continue
                 elif event.key == ord('2'):
                    TEXT=pygame.image.load('장면9-2.png')
                    PEOPLE = pygame.image.load('친구웃음.jpg')
                    PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
                    HEALTH = HEALTH +1 
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 12:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면10.png')
                    BACKGROUND=pygame.image.load('세종대학교.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 13:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면11.png')
                    #BACKGROUND=pygame.image.load('식당.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 14:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면12.png')
                    PEOPLE=pygame.image.load('음식.jpg')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 15:
                if event.key == ord('1'):
                    TEXT=pygame.image.load('장면12-1.png')
                    PEOPLE = pygame.image.load('안건강.jpg')
                    PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
                    HEALTH = HEALTH - 1
                    SCENE_NUM = SCENE_NUM + 1
                    continue
                elif event.key == ord('2'):
                    TEXT=pygame.image.load('장면12-2.png')
                    PEOPLE = pygame.image.load('건강.jpg')
                    PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
                    HEALTH = HEALTH + 1
                    SCENE_NUM = SCENE_NUM + 1
                    continue
                elif event.key == ord('3'):
                    TEXT=pygame.image.load('장면12-3.png')
                    PEOPLE = pygame.image.load('안건강.jpg')
                    PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
                    HEALTH = HEALTH - 1
                    SCENE_NUM = SCENE_NUM + 1
                    continue
                elif event.key == ord('4'):
                    TEXT=pygame.image.load('장면12-4.png')
                    PEOPLE = pygame.image.load('안건강.jpg')
                    PEOPLE = pygame.transform.scale(PEOPLE, (400,400))
                    HEALTH = HEALTH - 2
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 16:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면13.png')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 17:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면14.png')
                    SCENE_NUM = SCENE_NUM + 1
                    PEOPLE = pygame.image.load('건대생.jpg')
                    continue
            if SCENE_NUM == 18:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면15.png')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            if SCENE_NUM == 19:
                if event.key == pygame.K_SPACE:
                    TEXT=pygame.image.load('장면16.png')
                    SCENE_NUM = SCENE_NUM + 1
                    continue
            #if SCENE_NUM == 20:
                #밑에다가 미니게임 추가
            
            
            
           
                
            



        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
     
