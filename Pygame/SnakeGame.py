from tkinter import font, scrolledtext
import pygame, sys,random

speed = 7
size = 50
screen_x = 1200
screen_y = 700

error_check = pygame.init()
if error_check[1]>0:
    print("Error")
else:
    print("successful")
pygame.display.set_caption("Raj")
screen = pygame.display.set_mode((screen_x,screen_y))



def init_values():
    global direction, snake, snake_head, food_is,food_pos,score
    score = 0
    direction = "right"
    snake_head = [2*size,2*size]
    snake = [snake_head]
    food_is = True
    food_pos = [random.randrange(1,screen_x//size)*size,random.randrange(1,screen_y//size)*size]
init_values()
    
def handle_movement():
    if direction == "right":
        snake_head[0] += size
    elif direction == "left":
        snake_head[0] -= size
    elif direction == "up":
        snake_head[1] -= size
    elif direction == "down":
        snake_head[1] += size

    if snake_head[0]<0:snake_head[0] = screen_x - size
    elif snake_head[1]<0:snake_head[1] = screen_y - size
    elif snake_head[0]>screen_x - size:snake_head[0] = 0
    elif snake_head[1]>screen_y - size:snake_head[1] = 0    
def drawGFX():
    screen.fill("Black")
    for pos in snake:
        pygame.draw.rect(screen, "Green", pygame.Rect(pos[0] + 5 , pos[1] + 5,size -5, size -5 ))


    pygame.draw.rect(screen,"Red", pygame.Rect(food_pos[0], 
                    food_pos[1], size, size))
    
    Score_font = pygame.font.SysFont('consolas',20)
    # global Text
    Text = Score_font.render(f"Score: {score}",True,pygame.Color(255,255,255)).convert_alpha()
    screen.blit(Text,Text.get_rect(midtop = (screen_x / 2 ,screen_y - 50)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_UP and direction != "down" or key == pygame.K_w and direction != "down":direction = "up"
            if key == pygame.K_DOWN and direction != "up" or key == pygame.K_s and direction != "up":direction = "down"
            if key == pygame.K_RIGHT and direction != "left" or key == pygame.K_d and direction != "left":direction = "right"
            if key == pygame.K_LEFT and direction != "right" or key == pygame.K_a and direction != "right":direction = "left"

    handle_movement()
    
    snake.insert(0,list(snake_head))
    
    if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
        score +=1
        food_is = False
    else:
        snake.pop()
    if not food_is:
        food_pos = [random.randrange(0,screen_x//size)*size,random.randrange(0,screen_y//size)*size]
        
        food_is = True

    for i in snake[1:]:
        if i[1] == snake_head[1] and i[0] == snake_head[0]:
            init_values()
    

    drawGFX()
    pygame.display.update()
    pygame.time.Clock().tick(speed)#.as_integer_ratio().count()