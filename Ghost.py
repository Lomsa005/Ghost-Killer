from turtle import distance
import pygame
import random
import math
from pygame import RESIZABLE, mixer
#inicializeba
pygame.init()

#dapa tamashis
screen=pygame.display.set_mode((800,600))

startl=False

#background
background=pygame.image.load("images/back01.jpg")
background1=pygame.image.load("images/back2.jpg")
background2=pygame.image.load("images/back3.jpg")
background3=pygame.image.load("images/back.jpg")

clock = pygame.time.Clock()
m=0
#background sound
if m==0:
    mixer.music.load('music/background.wav')
    mixer.music.play(-1)
if m==1:
    mixer.music.load('music/music2.mp3')
    mixer.music.play(-1)
if m==2:
    mixer.music.load("music/music3.mp3")
    mixer.music.play(-1)
#saxelwodeba tamashis(title) da logo (icon)
pygame.display.set_caption("Ghost killer")
icon=pygame.image.load("images/carn.png")
pygame.display.set_icon(icon)

def game_end_back():
    end_back=pygame.image.load("images/back-end.jpg")
    screen.blit(end_back,(0,0))
    restart=pygame.image.load("images/restart.png")
    screen.blit(restart,(120,260))
#player
playerImg=pygame.image.load("images/ship.png")
playerX=370 
playerY=480
playerX_change=0
playerY_change=0
#player spaceship
playerImg_2=pygame.image.load('images/ship1.png')
playerX_2=335
playerY_2=510
playerX_change_1=0
playerY_change_1=0
#score 
score_value=0
font=pygame.font.Font('font/freesansbold.ttf', 32)
fontX=0
fontY=-10

#reaper
reap_x=1000
reap_x_1=-200
reap_x_t=False
reap_x_1_t=False
#game over txt
over_font=pygame.font.Font('font/freesansbold.ttf', 64)
sc_font=pygame.font.Font('font/freesansbold.ttf', 36)
sc_high_font=pygame.font.Font('font/freesansbold.ttf', 36)

def updateFile():
    f = open('h.s/highscore.txt','r') 
    file = f.readlines() 
    last = int(file[0]) 

    if int(last) > int(score_value): 
        sc=pygame.image.load('images/sc.png')
        high_score=sc_high_font.render(str(score_value),True,(230,130,37))
        screen.blit(sc,(180,230))
        screen.blit(high_score,(520,282))
        over_last=sc_font.render(str(last),True,(230,130,37))
        screen.blit(over_last,(520,368))
    else:      
        f.close()
        file = open('h.s/highscore.txt', 'w') 
        file.write(str(score_value)) 
        file.close() 
        sc_new=pygame.image.load('images/n_sc.png')
        over_score=sc_font.render(str(score_value),True,(230,130,37))
        screen.blit(over_score,(580,290))
        screen.blit(sc_new,(180,180))

def game_over_text():
    over_txt=pygame.image.load('images/untitled.png')
    screen.blit(over_txt,(150,20))
    updateFile()
    

def show_score(x,y):
    score_1=pygame.image.load('images/score.png')
    score=font.render(str(score_value),True,(230,150,37))
    screen.blit(score_1,(x,y))
    screen.blit(score,(x+110,y+22))

#enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
enemy_num=12
for i in range(enemy_num):
    enemyImg.append(pygame.image.load("images/lev1.png"))
    enemyImg.append(pygame.image.load("images/ghost.png"))
    enemyImg.append(pygame.image.load("images/lev0.png"))
    enemyX.append(random.randint(20,720))
    enemyY.append(random.randint(0,200))
    enemyX_change.append(5)
    enemyY_change.append(50)
#enemy2
enemyImg_1=pygame.image.load("images/lev4.png")
enemyX_1=random.randint(20,720)
enemyY_1=random.randint(0,200)
enemyX_change_1=9
enemyY_change_1=90

def enemy1(x,y):
    screen.blit(enemyImg_1,(x,y))

enemyImg_2=pygame.image.load("images/lev2.png")
enemyX_2=random.randint(20,720)
enemyY_2=random.randint(0,200)
enemyX_change_2=7
enemyY_change_2=80

def enemy2(x,y):
    screen.blit(enemyImg_2,(x,y))

enemyImg_3=pygame.image.load("images/lev3.png")
enemyX_3=random.randint(20,720)
enemyY_3=random.randint(0,100)
enemyX_change_3=2
enemyY_change_3=6

def enemy3(x,y):
    screen.blit(enemyImg_3,(x,y))
# bullet: ready- can't see bullet; fire- bullet is moving
bulletImg=pygame.image.load("images/bullet.png")
bulletX=0
bulletY=480
bulletX_change=0.2
bulletY_change=30
bullet_state='ready'

def bullet_fire(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+10,y+8))

bulletImg_1=pygame.image.load("images/bullet1.png")
bulletX_1=0
bulletY_1=510
bulletX_change_1=0.4
bulletY_change_1=37
bullet_state_1='ready'

def bullet_fire_1(x,y):
    global bullet_state_1
    bullet_state_1="fire"
    screen.blit(bulletImg_1,(x,y))

bulletImg_2=pygame.image.load("images/bullet2.png")
bulletX_2=0
bulletY_2=510
bulletX_change_2=0.4
bulletY_change_2=37
bullet_state_2='ready'

def bullet_fire_2(x,y):
    global bullet_state_2
    bullet_state_2="fire"
    screen.blit(bulletImg_2,(x,y))

bulletImg_3=pygame.image.load("images/bullet3.png")
bulletX_3=0
bulletY_3=510
bulletX_change_3=0.4
bulletY_change_3=40
bullet_state_3='ready'

def bullet_fire_3(x,y):
    global bullet_state_3
    bullet_state_3="fire"
    screen.blit(bulletImg_3,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))
def player1(x,y):
    screen.blit(playerImg_2,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def iscollision(enemyX,enemyY,bulletX,bulletY,reap_x_1,reap_x):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    k=math.sqrt((math.pow(enemyX-reap_x_1,2))+(math.pow(enemyY-280,2)))
    n=math.sqrt((math.pow(enemyX-reap_x,2))+(math.pow(enemyY-280,2)))
    if distance<27 or k<45 or n<45:
        return True
    else:
        return False
def iscollision_1(enemyX_2, enemyY_2, bulletX_1, bulletY_1,reap_x_1,reap_x):
    distance_1=math.sqrt((math.pow(enemyX_2-bulletX_1,2))+(math.pow(enemyY_2-bulletY_1,2)))
    k_1=math.sqrt((math.pow(enemyX_2-reap_x_1,2))+(math.pow(enemyY_2-280,2)))
    n_1=math.sqrt((math.pow(enemyX_2-reap_x,2))+(math.pow(enemyY_2-280,2)))
    if distance_1<35 or k_1<50 or n_1<50:
        return True
    else:
        return False
def iscollision_3(enemyX_3, enemyY_3, bulletX_3, bulletY_3,reap_x_1,reap_x):
    distance_3=math.sqrt((math.pow(enemyX_3-bulletX_3,2))+(math.pow(enemyY_3-bulletY_3,2)))
    k_3=math.sqrt((math.pow(enemyX_3-reap_x_1,2))+(math.pow(enemyY_3-280,2)))
    n_3=math.sqrt((math.pow(enemyX_3-reap_x,2))+(math.pow(enemyY_3-280,2)))
    if distance_3<35 or k_3<50 or n_3<50:
        return True
    else:
        return False
def iscollision_2(enemyX_1, enemyY_1, bulletX_2, bulletY_2,reap_x_1,reap_x):
    distance_2=math.sqrt((math.pow(enemyX_1-bulletX_2,2))+(math.pow(enemyY_1-bulletY_2,2)))
    k_2=math.sqrt((math.pow(enemyX_1-reap_x_1,2))+(math.pow(enemyY_1-280,2)))
    n_2=math.sqrt((math.pow(enemyX_1-reap_x,2))+(math.pow(enemyY_1-280,2)))
    if distance_2<35 or k_2<50 or n_2<50:
        return True
    else:
        return False
def iscollision_end(enemyX,enemyY,playerX,playerY):
    distanc=math.sqrt((math.pow(enemyX-playerX,2))+(math.pow(enemyY-playerY,2)))
    if distanc<50:
        return True
    else:
        return False
def iscollision_end_1(enemyX_2,enemyY_2,playerX,playerY):
    distanc_1=math.sqrt((math.pow(enemyX_2-playerX,2))+(math.pow(enemyY_2-playerY,2)))
    if distanc_1<50:
        return True
    else:
        return False
def iscollision_end_3(enemyX_3,enemyY_3,playerX,playerY):
    distanc_4=math.sqrt((math.pow(enemyX_3-playerX,2))+(math.pow(enemyY_3-playerY,2)))
    if distanc_4<50:
        return True
    else:
        return False
def iscollision_end_2(enemyX_1,enemyY_1,playerX,playerY):
    distanc_2=math.sqrt((math.pow(enemyX_1-playerX,2))+(math.pow(enemyY_1-playerY,2)))
    if distanc_2<50:
        return True
    else:
        return False

m=0
k=0
#tamashis ar gatishva sanam momxmarebeli ar daawers X -s 

running=True
while running:
    #background color
    if k==0:
        screen.fill((255,255,153))
        screen.blit(background1,(0,0))
    #background image
    elif k==1:
            screen.fill((255,255,153))
            screen.blit(background,(0,0))
    elif k==2:
            screen.fill((255,255,153))
            screen.blit(background2,(0,0))
    elif k==3:
            screen.fill((255,255,153))
            screen.blit(background3,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                startl=True
                def game_end_back():
                    end_back=pygame.image.load("images/back-end.jpg")
                    screen.blit(end_back,(0,0))
                    restart=pygame.image.load("images/restart.png")
                    screen.blit(restart,(120,260))
                #player
                playerImg=pygame.image.load("images/ship.png")
                playerX=370 
                playerY=480
                playerX_change=0
                playerY_change=0
                #player spaceship
                playerImg_2=pygame.image.load('images/ship1.png')
                playerX_2=335
                playerY_2=510
                playerX_change_1=0
                playerY_change_1=0
                #score 
                score_value=0
                font=pygame.font.Font('font/freesansbold.ttf', 32)
                fontX=0
                fontY=-10

                #reaper
                reap_x=1000
                reap_x_1=-200
                reap_x_t=False
                reap_x_1_t=False
                #game over txt
                over_font=pygame.font.Font('font/freesansbold.ttf', 64)
                sc_font=pygame.font.Font('font/freesansbold.ttf', 36)
                sc_high_font=pygame.font.Font('font/freesansbold.ttf', 36)

                def updateFile():
                    f = open('h.s/highscore.txt','r') 
                    file = f.readlines() 
                    last = int(file[0]) 

                    if int(last) > int(score_value): 
                        sc=pygame.image.load('images/sc.png')
                        high_score=sc_high_font.render(str(score_value),True,(230,130,37))
                        screen.blit(sc,(180,240))
                        screen.blit(high_score,(520,282))
                        over_last=sc_font.render(str(last),True,(230,130,37))
                        screen.blit(over_last,(520,368))
                    else:      
                        f.close()
                        file = open('h.s/highscore.txt', 'w') 
                        file.write(str(score_value)) 
                        file.close() 
                        sc_new=pygame.image.load('images/n_sc.png')
                        over_score=sc_font.render(str(score_value),True,(230,130,37))
                        screen.blit(over_score,(580,290))
                        screen.blit(sc_new,(180,190))

                def game_over_text():
                    over_txt=pygame.image.load('images/untitled.png')
                    screen.blit(over_txt,(150,20))
                    updateFile()
                    

                def show_score(x,y):
                    score_1=pygame.image.load('images/score.png')
                    score=font.render(str(score_value),True,(230,150,37))
                    screen.blit(score_1,(x,y))
                    screen.blit(score,(x+110,y+22))

                #enemy
                enemyImg=[]
                enemyX=[]
                enemyY=[]
                enemyX_change=[]
                enemyY_change=[]
                enemy_num=12
                for i in range(enemy_num):
                    enemyImg.append(pygame.image.load("images/lev1.png"))
                    enemyImg.append(pygame.image.load("images/ghost.png"))
                    enemyImg.append(pygame.image.load("images/lev0.png"))
                    enemyX.append(random.randint(20,720))
                    enemyY.append(random.randint(0,200))
                    enemyX_change.append(5)
                    enemyY_change.append(50)
                #enemy2
                enemyImg_1=pygame.image.load("images/lev4.png")
                enemyX_1=random.randint(20,720)
                enemyY_1=random.randint(0,200)
                enemyX_change_1=9
                enemyY_change_1=90

                def enemy1(x,y):
                    screen.blit(enemyImg_1,(x,y))

                enemyImg_2=pygame.image.load("images/lev2.png")
                enemyX_2=random.randint(20,720)
                enemyY_2=random.randint(0,200)
                enemyX_change_2=7
                enemyY_change_2=80

                def enemy2(x,y):
                    screen.blit(enemyImg_2,(x,y))

                enemyImg_3=pygame.image.load("images/lev3.png")
                enemyX_3=random.randint(20,720)
                enemyY_3=random.randint(0,100)
                enemyX_change_3=2
                enemyY_change_3=6

                def enemy3(x,y):
                    screen.blit(enemyImg_3,(x,y))
                # bullet: ready- can't see bullet; fire- bullet is moving
                bulletImg=pygame.image.load("images/bullet.png")
                bulletX=0
                bulletY=480
                bulletX_change=0.2
                bulletY_change=30
                bullet_state='ready'

                def bullet_fire(x,y):
                    global bullet_state
                    bullet_state="fire"
                    screen.blit(bulletImg,(x+10,y+8))

                bulletImg_1=pygame.image.load("images/bullet1.png")
                bulletX_1=0
                bulletY_1=510
                bulletX_change_1=0.4
                bulletY_change_1=37
                bullet_state_1='ready'

                def bullet_fire_1(x,y):
                    global bullet_state_1
                    bullet_state_1="fire"
                    screen.blit(bulletImg_1,(x,y))

                bulletImg_2=pygame.image.load("images/bullet2.png")
                bulletX_2=0
                bulletY_2=510
                bulletX_change_2=0.4
                bulletY_change_2=37
                bullet_state_2='ready'

                def bullet_fire_2(x,y):
                    global bullet_state_2
                    bullet_state_2="fire"
                    screen.blit(bulletImg_2,(x,y))

                bulletImg_3=pygame.image.load("images/bullet3.png")
                bulletX_3=0
                bulletY_3=510
                bulletX_change_3=0.4
                bulletY_change_3=40
                bullet_state_3='ready'

                def bullet_fire_3(x,y):
                    global bullet_state_3
                    bullet_state_3="fire"
                    screen.blit(bulletImg_3,(x,y))

                def player(x,y):
                    screen.blit(playerImg,(x,y))
                def player1(x,y):
                    screen.blit(playerImg_2,(x,y))

                def enemy(x,y,i):
                    screen.blit(enemyImg[i],(x,y))
                m=0
                k=0
    #klavishebis moqmebdeba
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_b:
                k=k+1
                if k>3:
                    k=0
                
                 
            if event.key==pygame.K_m:
                m=m+1
                if m==1:
                    mixer.music.unload()
                    mixer.music.load('music/music1.mp3')
                    mixer.music.play(-1)
                elif m==2:
                    mixer.music.unload()
                    mixer.music.load('music/music2.mp3')
                    mixer.music.play(-1)
                elif m==3:
                    mixer.music.unload()
                    mixer.music.load('music/music3.mp3')
                    mixer.music.play(-1)
                elif m==4:
                    mixer.music.unload()
                    mixer.music.load('music/background.wav')
                    mixer.music.play(-1)
                elif m>4:
                    m=0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if score_value>50 and score_value<100:
                    playerX_change=-10
                    playerX_change_1=-10
                elif score_value>100 and score_value<150:
                    playerX_change=-11
                    playerX_change_1=-11
                elif score_value>150:
                    playerX_change=-12
                    playerX_change_1=-12
                else:
                    playerX_change=-8
                    playerX_change_1=-8
            if event.key==pygame.K_RIGHT:
                if score_value>50 and score_value<100:
                    playerX_change=10
                    playerX_change_1=10
                elif score_value>100 and score_value<150:
                    playerX_change=11
                    playerX_change_1=11
                elif score_value>150:
                    playerX_change=12
                    playerX_change_1=12
                else:
                    playerX_change=8
                    playerX_change_1=8
            if event.key==pygame.K_UP:
                if score_value>50 and score_value<100:
                    playerY_change=-8
                    playerY_change_1=-8
                elif score_value>100 and score_value<150:
                    playerY_change=-9
                    playerY_change_1=-9
                elif score_value>150:
                    playerY_change=-10
                    playerY_change_1=-10
                else:
                    playerY_change=-7
                    playerY_change_1=-7
            if event.key==pygame.K_DOWN:
                if score_value>50 and score_value<100:
                    playerY_change=8
                    playerY_change_1=8
                elif score_value>100 and score_value<150:
                    playerY_change=9
                    playerY_change_1=9
                elif score_value>150:
                    playerY_change=10
                    playerY_change_1=10
                else:
                    playerY_change=7
                    playerY_change_1=7
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bullet_sound =mixer.Sound('voice/laser.wav')
                    bullet_sound.play()
                    bulletY=playerY
                    bulletX=playerX
                    bullet_fire(bulletX,bulletY)
            if event.key==pygame.K_z:
                if score_value>20:
                    if bullet_state_1=="ready":
                        bullet_sound_1 =mixer.Sound('voice/gun1.mp3')
                        bullet_sound_1.play()
                        bulletY_1=playerY_2
                        bulletX_1=playerX_2
                        bullet_fire_1(bulletX_1,bulletY_1)
            if event.key==pygame.K_x:
                if score_value>100:
                    if bullet_state_2=="ready":
                        bullet_sound_2 =mixer.Sound('voice/gun2.mp3')
                        bullet_sound_2.play()
                        bulletY_2=playerY_2
                        bulletX_2=playerX_2
                        bullet_fire_2(bulletX_2,bulletY_2)
            if event.key==pygame.K_c:
                if score_value>150:
                    if bullet_state_3=="ready":
                        bullet_sound_3 =mixer.Sound('voice/gun3.mp3')
                        bullet_sound_3.play()
                        bulletY_3=playerY_2
                        bulletX_3=playerX_2
                        bullet_fire_3(bulletX_3,bulletY_3)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerX_change=0
                playerY_change=0
                playerX_change_1=0
                playerY_change_1=0
    for i in range(enemy_num):
        #game over
        end=iscollision_end(enemyX[i],enemyY[i],playerX,playerY)
        if end==True:
            playerX_change=0
            playerY_change=0
            playerX+=0
            playerY+=0
            playerX_change_1=0
            playerY_change_1=0
            playerX_2+=0
            playerY_2+=0
            bullet_state='ready'
            bullet_state_1='ready'
            bullet_state_2='ready'
            bullet_state_3='ready'
            fontX=-100
            fontY=-100
            enemyY_3+=0
            enemyX_3+=0
            enemyX_change_3=0
            enemyY_change_3=0
            pygame.mixer.stop()
            for k in range(enemy_num):
                enemyX_change[k]=0
                enemyY_change[k]=0
    #enemy is moqmedeba da sazgvrebs ro ar gacdes.
        else: 
            enemyX[i]+=enemyX_change[i]
            if enemyX[i]<=20:
                enemyX_change[i]=5
                enemyY[i]+=enemyY_change[i]
            elif enemyX[i]>=720:
                enemyX_change[i]=-5
                enemyY[i]+=enemyY_change[i]
            if enemyX[i]>=719 and enemyY[i]>=680:
                enemyX[i]=random.randint(20,720)
                enemyY[i]=random.randint(0,300) 
            #shejaxeba
            collision=iscollision(enemyX[i], enemyY[i], bulletX, bulletY,reap_x_1,reap_x)
            if collision:
                bulletY=480
                bullet_state="ready"
                score_value+=1
                enemyX[i]=random.randint(20,720)
                enemyY[i]=random.randint(0,300) 
            enemy(enemyX[i],enemyY[i],i)
    if score_value>20:
            end_1=iscollision_end_1(enemyX_2,enemyY_2,playerX,playerY) 
            if end_1==True:
                enemyX_change_2=0
                enemyY_change_2=0
                enemyY_3+=0
                enemyX_3+=0
                enemyX_change_3=0
                enemyY_change_3=0
            else: 
                enemyX_2+=enemyX_change_2
                if enemyX_2<=20:
                    if score_value>50:
                        enemyX_change_2=8
                        enemyY_2+=enemyY_change_2
                    elif score_value>100:
                        enemyX_change_2=9
                        enemyY_2+=enemyY_change_2
                    else:
                        enemyX_change_2=7
                        enemyY_2+=enemyY_change_2
                elif enemyX_2>=720:
                    if score_value>50:
                        enemyX_change_2=-8
                        enemyY_2+=enemyY_change_2
                    elif score_value>100:
                        enemyX_change_2=-9
                        enemyY_2+=enemyY_change_2
                    else:
                        enemyX_change_2=-7
                        enemyY_2+=enemyY_change_2
                if enemyX_2>=719 and enemyY_2>=680:
                    enemyX_2=random.randint(20,720)
                    enemyY_2=random.randint(0,200)
                    #shejaxeba
                collision_1=iscollision_1(enemyX_2, enemyY_2, bulletX_1, bulletY_1,reap_x_1,reap_x)
                if collision_1:
                    bulletY_1=510
                    bullet_state_1="ready"
                    score_value+=2
                    enemyX_2=random.randint(20,720)
                    enemyY_2=random.randint(0,200) 
                enemy2(enemyX_2,enemyY_2)
    if score_value>100:
            end_2=iscollision_end_2(enemyX_1,enemyY_1,playerX,playerY) 
            if end_2==True:
                enemyX_change_1=0
                enemyY_change_1=0
                playerX_change_1=0
                playerY_change_1=0
                playerX_2+=0
                playerY_2+=0
                enemyY_3+=0
                enemyX_3+=0
                enemyX_change_3=0
                enemyY_change_3=0
            else:
                enemyX_1-=enemyX_change_1
                if enemyX_1<=20:
                    enemyX_change_1=-8
                    enemyY_1+=enemyY_change_1
                elif enemyX_1>=720:
                    enemyX_change_1=8
                    enemyY_1+=enemyY_change_1
                if enemyX_1>=719 and enemyY_1>=680:
                    enemyX_1=random.randint(20,720)
                    enemyY_1=random.randint(0,200)
                    #shejaxeba
                collision_2=iscollision_2(enemyX_1, enemyY_1, bulletX_2, bulletY_2,reap_x_1,reap_x)
                if collision_2:
                    bulletY_2=510
                    bullet_state_2="ready"
                    score_value+=3
                    enemyX_1=random.randint(20,720)
                    enemyY_1=random.randint(0,200) 
                enemy1(enemyX_1,enemyY_1)
    if score_value>150:
            ene_3=True
            end_3=iscollision_end_3(enemyX_3,enemyY_3,playerX,playerY) 
            end_1=iscollision_end_1(enemyX_2,enemyY_2,playerX,playerY) 
            end_2=iscollision_end_2(enemyX_1,enemyY_1,playerX,playerY)
            for i in range(enemy_num):
                end=iscollision_end(enemyX[i],enemyY[i],playerX,playerY)
                if end==True:
                    enemyX_change_3=0
                    enemyY_change_3=0
                    playerX_change=0
                    playerY_change=0
                    playerX_change_1=0
                    playerY_change_1=0
                    enemyY_3+=0
                    enemyX_3+=0
                    ene_3=False
            if end_1==True or end_2==True or end_3==True:
                enemyX_change_3=0
                enemyY_change_3=0
                playerX_change=0
                playerY_change=0
                playerX_change_1=0
                playerY_change_1=0
                enemyY_3+=0
                enemyX_3+=0
                reap_x_ch=0
                reap_x_ch_1=0
                reap_x=-100
                reap_x_1=1000
                ene_3=False
            if ene_3==True:
                if score_value>=150 and score_value<153:
                    enemy_sound_1=mixer.Sound('voice/level3.wav')
                    enemy_sound_1.play(0)
                enemyY_3+=enemyY_change_3
                if enemyY_3<=600:
                    if score_value>400:
                        enemyY_change_3=6
                        enemyY_3+=enemyY_change_3
                    else:
                        enemyY_change_3=5
                        enemyY_3+=enemyY_change_3
                elif enemyY_3>=0:
                    enemyY_change_3=-5
                    enemyX_3+=enemyX_change_3
                    enemyX_3=random.randint(20,720)
                    enemyY_3=random.randint(0,100)
                    #shejaxeba
                collision_3=iscollision_3(enemyX_3, enemyY_3, bulletX_3, bulletY_3,reap_x_1,reap_x)
                if collision_3:
                    bulletY_1=510
                    bullet_state_3="ready"
                    score_value+=5
                    enemyX_3=random.randint(20,720)
                    enemyY_3=random.randint(0,100) 
                enemy3(enemyX_3,enemyY_3)
    #player is moqmedeba da sazgvrebs ro ar gacdes.
    playerX+=playerX_change
    if playerX<=35:
        playerX=35
    elif playerX>=736:
        playerX=736
    playerY+=playerY_change
    if playerY<=300:
        playerY=300
    elif playerY>=521:
        playerY=521
    
    playerX_2+=playerX_change_1
    if playerX_2<=0:
        playerX_2=0
    elif playerX_2>=701:
        playerX_2=701
    playerY_2+=playerY_change_1
    if playerY_2<=330:
        playerY_2=330
    elif playerY_2>=551:
        playerY_2=551

    #reaper
    if score_value>180 and reap_x>-100:
        reap=pygame.image.load("images/reap.png")            
        reap_x_ch=-5
        def reaper(x):
            screen.blit(reap,(x,280))
        reap_x_t=True
    if score_value>360 and reap_x_1<900:
        reap1=pygame.image.load("images/reap1.png")
        reap_x_ch_1=5
        def reaper1(x):
            screen.blit(reap1,(x,280))
        reap_x_1_t=True

    #bullet is modzraoba
    if bulletY<=0:
        bulletY=480
        bullet_state='ready'
    if bullet_state =='fire':
        bullet_fire(bulletX,bulletY)
        bulletY-=bulletY_change
    
    if bulletY_1<=0:
            bulletY_1=510
            bullet_state_1='ready'
    if bullet_state_1 =='fire':
            bullet_fire_1(bulletX_1,bulletY_1)
            bulletY_1-=bulletY_change_1
    if bulletY_2<=0:
            bulletY_2=510
            bullet_state_2='ready'
    if bullet_state_2 =='fire':
            bullet_fire_2(bulletX_2,bulletY_2)
            bulletY_2-=bulletY_change_2
    if bulletY_3<=0:
            bulletY_3=510
            bullet_state_3='ready'
    if bullet_state_3 =='fire':
            bullet_fire_3(bulletX_3,bulletY_3)
            bulletY_3-=bulletY_change_3
    #funqciis gamodzaxeba da tamashi ro moqmedebashi iyos
    player(playerX,playerY)
    player1(playerX_2,playerY_2)
    show_score(fontX,fontY)
    if score_value>180 and reap_x_t==True:
        reap_x_ch=-5
        reap_x+=reap_x_ch
        reaper(reap_x)
    if score_value>360 and reap_x_1_t==True:
        reap_x_ch_1=5
        reap_x_1+=reap_x_ch_1
        reaper1(reap_x_1)
    for i in range(enemy_num):
        #game over
        end_1=iscollision_end_1(enemyX_2,enemyY_2,playerX,playerY) 
        end_2=iscollision_end_2(enemyX_1,enemyY_1,playerX,playerY)
        end=iscollision_end(enemyX[i],enemyY[i],playerX,playerY)
        end_3=iscollision_end_3(enemyX_3,enemyY_3,playerX,playerY)
        if end==True or end_1==True or end_2==True or end_3==True:
            playerX_change=0
            playerY_change=0
            playerX+=0
            playerY+=0
            playerX_change_1=0
            playerY_change_1=0
            playerX_2+=0
            playerY_2+=0
            bullet_state='ready'
            bullet_state_1='ready'
            bullet_state_2='ready'
            bullet_state_3='ready'
            fontX=-100
            fontY=-100
            enemyY_change_3=0
            enemyX_change_2=0
            enemyX_change_2=0 
            enemyY_change_1=0
            enemyX_change_1=0
            enemyX_change_3=0
            enemyY_3+=0
            enemyX_3+=0
            reap_x_ch=0
            reap_x_ch_1=0
            reap_x=-100
            reap_x_1=1000
            pygame.mixer.stop()
            for k in range(enemy_num):
                enemyX_change[k]=0
                enemyY_change[k]=0
            game_end_back()
            game_over_text()
    clock.tick(30)
    if startl==False:
        starti=pygame.image.load("images/start.jpg")
        screen.blit(starti,(0,0))
    pygame.display.update()