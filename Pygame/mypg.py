import pygame
from sys import exit
import sys

pygame.init()

screen = pygame.display.set_mode((800,400))
dis = pygame.display

dis.set_caption('pyGame')
s3_x = 799
velocity1 = 1*2
s1 = pygame.image.load('py\pg\skky.jpg').convert()
s2 = pygame.image.load('py\pg\gd.jpg').convert()
s3 = pygame.image.load('py\pg\snail1.png').convert_alpha()
s5 = pygame.image.load('py\pg\snail2.png').convert_alpha()

s4 = pygame.image.load('py\pg\plwk2.png').convert_alpha()
clock = pygame.time.Clock()
s4_x= 100
font = pygame.font.Font('py\pg\Pixeltype.ttf',50)

velocity2 = 0
h = 0
a = 0
b = 0
c = 300
cj = 0.0000
aa =False
s3_x2 = 399

x2 = 399
while h < 4001:
    m = '{:.3f}'.format(cj)
    text1 = font.render(f"Death: {a}    Score: {b}   AVG: {m}",False,'Black')
    s4_t = s4.get_rect(midbottom = [s4_x,c])
    s3_t = s3.get_rect(midbottom=(s3_x,300))
    s3_t2 = s5.get_rect(midbottom=(x2,200))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(s1,(0,0))
    screen.blit(s2,(0,300))
    screen.blit(text1,(200,50))
    screen.blit(s3,s3_t)
    screen.blit(s5,s3_t2)

    screen.blit(s4,s4_t)
    speed = 3
    s3_x -= velocity1
    x2 -= velocity1
    
    #s4
    if pygame.mouse.get_pressed() == (False,True,False) and c != 203 and c > 203:
        for i in range(40):
            c+=-0.25
        aa = True
        speed = 6

    if pygame.mouse.get_pressed() == (False,False,False) and aa:
            
            
            for i in range(20):
                c+=0.5
            if c == 300:
                aa = False
    if pygame.mouse.get_pressed() == (True,False,False):
        velocity2 = -1 * speed
    if pygame.mouse.get_pressed() == (False,False,True):
        velocity2 = 1* speed
            

            

        
        
    
    print(h)
    s4_x += velocity2
    if s4_t.collidepoint(s3_t.topleft):
        s4_x = 100
        s3_x = 799
        velocity2 =0
        a += 1

   
    if s4_t.collidepoint(s3_t.topright):
        s4_x = 100
        s3_x = 799
        velocity2 =0
        a += 1

    
    if s4_t.collidepoint(s3_t.midtop):
        s4_x = 100
        s3_x = 799
        velocity2 =0
        a += 1

    if s4_t.collidepoint(s3_t2.topleft):
        s4_x = 100
        x2 = 799
        velocity2 =0
        a += 1
    if s4_t.collidepoint(s3_t2.topright):
        s4_x = 100
        x2 = 799
        velocity2 =0
        a += 1
    if s4_t.collidepoint(s3_t2.bottomleft):
        s4_x = 100
        x2 = 799
        velocity2 =0
        a += 1
    if s4_t.collidepoint(s3_t2.bottomleft):
        s4_x = 100
        x2 = 799
        velocity2 =0
        a += 1
    if s3_x <= -100:
        s3_x = 805
        b += 1
    
    if s4_t.left >= 800:
        s4_x = 1
    if s4_t.right <= -1:
        s4_x = 800
    
    if x2 <= -100:
        x2 = 805
        b+=1
    if a != 0 and b!=0:
        cj = b/a
    h += 1




    pygame.display.update()
    
    clock.tick(60)
print(f"\n\n\nScore: {cj}\n\n\n")