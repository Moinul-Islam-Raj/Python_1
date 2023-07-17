import pygame as pg
from sys import exit

def animation():
	global player_index,player_surf,player_surfs,player_rect,all_ani
	player_index +=all_ani_2
	
	if player_index >= len(player_surfs):player_index = 0
	if player_rect.bottom < 300: player_surf = player_surfs[0]
	else:player_surf = player_surfs[int(player_index)]
	
def animation_fly():
	global fly_index,fly_surfs,fly_surf_all,fly_surf,fly_surf_2,all_ani
	fly_index += all_ani
	
	if fly_index >= len(fly_surfs):fly_index = 0
	fly_surf_all = fly_surfs[int(fly_index)]
	fly_surf = fly_surf_all
	fly_surf_2 = fly_surf_all
def animation_snail():
	global snail_index,snail_surfs,snail_surf_0,snail_surf,snail_surf_2,snail_ani
	snail_index += snail_ani
	
	if snail_index >= len(snail_surfs):snail_index = 0
	snail_surf_0 = snail_surfs[int(snail_index)]
	snail_surf = snail_surf_0
	snail_surf_2 = snail_surf_0




pg.init()
screen = pg.display.set_mode((800,400))
font = pg.font.Font('py\mypg\Pixeltype.ttf',55)
pg.display.set_caption('Jump Game Made By Raj')

#Values
Score = 0
gravity = 0
isActive = True
Highscore = 0
loop = 0
player_index = 0
fly_index = 0
snail_index = 0
Start_time = 0
object_speed = 5
all_ani= 0.1
all_ani_2 = 0.1
snail_ani= 0.2
player_speed = 2
jump_force = 20
fly_y = 170

#Unmovable surfaces
sky_surf = pg.image.load('py\mypg\skky.jpg').convert()
ground_surf = pg.image.load('py\mypg\gd.jpg').convert()
text = font.render(f'Score: {Score}  Highscore: {Highscore}',False,'Black').convert()
#sound
jump_sound = pg.mixer.Sound('py\mypg\\audio_jump.mp3')
jump_sound.set_volume(0.5)

bg_sound = pg.mixer.Sound('py\mypg\music.wav')
bg_sound.set_volume(0.5)
bg_sound.play(loops = -1)
#movable surfs
player_1 = pg.image.load('py\mypg\plwk2.png').convert_alpha()
player_2 = pg.image.load('py\mypg\plwk.png').convert_alpha()
player_surfs = [player_1,player_2]
player_surf = player_surfs[player_index]


snail_surfs = [pg.image.load('py\mypg\snail1.png'),pg.image.load('py\mypg\snail4.png')]
snail_surf_0 = snail_surfs[snail_index]
snail_surf = snail_surf_0
snail_surf_2 = snail_surf_0


fly_surfs = [pg.image.load('py\mypg\snail2.png'),pg.image.load('py\mypg\snail3.png')]
fly_surf_all = fly_surfs[fly_index]
fly_surf = fly_surf_all
fly_surf_2 = fly_surf_all


#Rectangles
text_rect = text.get_rect(center = (400,50))
fly_rect = fly_surf.get_rect(midbottom = (1000,fly_y))
fly_rect_2 = fly_surf_2.get_rect(midbottom = (1440,fly_y))
player_rect = player_surf.get_rect(midbottom = (100,300))
snail_rect = snail_surf.get_rect(midbottom = (800,300))

snail_rect_2 = snail_surf_2.get_rect(midbottom = (1255,300))
while True:
    fly_rect.y = fly_y
    fly_rect_2.y = fly_y
    

    animation_snail()
    animation_fly()
    #Loop Default Values
    player_velocity = 0

    #Scoe Text
    text = font.render(f'Score: {Score}  Highscore: {Highscore}',False,'Black').convert()
    #Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN and isActive:
            if player_rect.bottom ==300 :  
                if event.key ==  pg.K_SPACE or event.key == pg.K_w or event.key == pg.K_UP:
                    gravity = -jump_force
                    jump_sound.play()
            if event.key == pg.K_0:
                if object_speed <=4.5:jump_force -= 0.5
                else: jump_force -= 1/7*5
                object_speed += 0.5
                snail_ani += 0.2*(10/100)
                all_ani += 0.1*(10/100)
                player_speed -= 0.30
                all_ani_2 -= 0.1*(10/100)
                fly_y +=1/7*45

                if fly_y >= 170: fly_y = 170
                if object_speed >= 7.5:object_speed = 7.5
                if all_ani >= 0.1 + 0.1*(70/100) or all_ani_2 >= 0.1 - 0.1*(30/100):all_ani = 0.1 + 0.1*(70/100);all_ani_2 = 0.1 - 0.1*(30/100)
                if snail_ani >= 0.2 + 0.2*(70/100):snail_ani = 0.2 + 0.2*(70/100)
                if player_speed <= 1: player_speed= 1
                if jump_force <= 14.99999:jump_force=14.99999


            if event.key == pg.K_9:
                object_speed -= 0.5
                snail_ani -= 0.2*(10/100)
                all_ani -= 0.1*(10/100)
                player_speed += 0.45
                all_ani_2 += 0.1*(10/100)
                if object_speed >= 5.5:jump_force +=  1/7*5.11111
                else:jump_force +=0.5
                if object_speed <= 5 :fly_y -=1/6*45


                if fly_y <= 125:fly_y =125
                if object_speed <= 2:object_speed = 2
                if all_ani <= 0.1 - 0.1*(60/100) or all_ani_2 >= 0.1 + 0.1*(60/100):all_ani = 0.1 - 0.1*(60/100);all_ani_2 = 0.1 + 0.1*(60/100)
                if snail_ani <= 0.2 - 0.2*(60/100):snail_ani = 0.2 - 0.2*(60/100)
                if player_speed >= 2 + 6*0.45: player_speed= 2 + 6*0.45
                if jump_force >= 23.0:jump_force=23.0

            # if event.key ==  pg.K_a:player_velocity -=8
            # if event.key ==  pg.K_d:player_velocity +=8
            if event.key ==  pg.K_ESCAPE:
                pg.quit()
                exit()
        if event.type == pg.KEYDOWN:
            isActive = True
    # Main Game
    if isActive:
        print(jump_force)
        bg_sound.set_volume(0.5)
        #Unmovable surfaces
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))
        screen.blit(text,text_rect)

        #movable surfs
        snail_rect.x -=object_speed
        screen.blit(snail_surf,snail_rect)
        snail_rect_2.x -=object_speed
        screen.blit(snail_surf_2,snail_rect_2)

        fly_rect.x -= object_speed
        screen.blit(fly_surf,fly_rect)
        fly_rect_2.x -= object_speed
        screen.blit(fly_surf_2,fly_rect_2)

        screen.blit(player_surf,player_rect)

        #player jump
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            player_rect.x += -player_speed
            animation()
        if keys[pg.K_d]:
            player_rect.x += player_speed
            animation()
        if keys[pg.K_RIGHT]:
            player_rect.x += player_speed
            animation()
        if keys[pg.K_LEFT]:
            player_rect.x += -player_speed
            animation()

        gravity += 1.15
        player_rect.y +=gravity
        
        if player_rect.bottom >= 300:player_rect.bottom = 300
        player_rect.x += player_velocity
        #collison logic
        if player_rect.colliderect(snail_rect) or player_rect.colliderect(fly_rect) or player_rect.colliderect(fly_rect_2) or player_rect.colliderect(snail_rect_2):
            isActive = False

        #   player
        if player_rect.left <= 0:
            player_rect.left = 0
            
        if player_rect.right >= 800:
            player_rect.right = 800
            

        #   snail
        if snail_rect.right <=0:
            snail_rect.left = 800
            
            
        #   snail_2
        if snail_rect_2.right <=0:
            snail_rect_2.left = 800
            
            
        #   fly
        if fly_rect.right <=0:
            fly_rect.left = 800
           
            
        #   fly_2
        if fly_rect_2.right <=0:
            fly_rect_2.left = 800
            
        Score = int(pg.time.get_ticks()/1000) - Start_time

        if Score >= Highscore: Highscore = Score
        Score1 = Score
    else:
        object_speed = 5
        snail_ani = 0.2
        all_ani = 0.1
        all_ani_2 = 0.1
        player_speed = 2
        jump_force = 20
        fly_y = 170

        bg_sound.set_volume(0)
        Start_time = int(pg.time.get_ticks()/1000)
        screen.fill((230,230,230))
        snail_rect.left = 800
        fly_rect.left = 1000
        fly_rect_2.left = 1430
        snail_rect_2.left = 1255
        player_rect.x = 100
        

        text_3 = font.render(f'Score: {Score1}',False,40)
        text_3_rect = text_3.get_rect(midtop = (400,330))
        Score = 0
        text_2 = font.render('Press any key to continue',False,70)
        text_2_rect = text_2.get_rect(midtop = (400,50))
        screen.blit(text_2,text_2_rect)
        screen.blit(player_surf,(350,150))
        screen.blit(text_3,text_3_rect)

    #Update Game
    loop += 1
    pg.display.update()
    pg.time.Clock().tick(60)