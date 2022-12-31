#importing libraries
import pygame
import time
import random

#initiliaze pygame
pygame.init()

#window size
window = pygame.display.set_mode((900,600))
pygame.display.flip()

icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
#window title
pygame.display.set_caption("Snake Game")
#snake
snake_x = 55
snake_y = 90
snake_pos = [snake_x , snake_y]
velocity_x = 0
velocity_y = 0
snake_size = 15
# snake_size_change = 0

#food 
food_x = random.randint(20,900/2)
food_y = random.randint(0,600/2)
food_size = 15

#score
score = 0
score_pos_x = 30
score_pos_y = 20
font = pygame.font.Font('li.ttf', 30)
def score_show(x, y):
    score_value = font.render('Score: ' + str(score), True, (blue))
    window.blit(score_value,(x,y))

def plot_snake(window, color,snake_list,snake_size):
    for snakex, snakey in snake_list:
       pygame.draw.rect(window, color, [snakex, snakey,snake_size,snake_size])

def game_over():
   
    # creating font object my_font
    my_font = pygame.font.Font('li.ttf', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    # game_over_surface1 = my_font.render(
    #     'Press Enter' , True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    # game_over_rect1 = game_over_surface1.get_rect()
    # setting position of the text
    game_over_rect.midtop = (900/2, 600/4)
     
    # blit will draw the text on screen
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
    # if x< -1:
    #     print("game_over!")
    # if y< -1 or y>=600:
    #     print("game_over!")

#snake length
snake_list = []
snake_length = 1

fps = 50
clock = pygame.time.Clock()
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
running = True
while running:
    # if check_collids:
    #     window.fill(white)
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x =5
                velocity_y =0
            if event.key == pygame.K_LEFT:
                velocity_x = -5
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -5
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y =5
                velocity_x = 0
        snake_x = snake_x +velocity_x
        snake_y = snake_y +velocity_y
        if snake_x <0 or snake_x>=900:
            game_over()
        if snake_y <0 or snake_y>=600:
            game_over()
        
        if abs(snake_x - food_x)< 8 and abs(snake_y - food_y)<8:
            score +=10
            food_x = random.randint(20,900/2)
            food_y = random.randint(25,600/2)
            snake_length+=5
            pygame.draw.rect(window, black, [snake_x,snake_y,snake_size_change,snake_size])


            # if event.type==pygame.KEYUP:
            #     if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         snake_x =0
            
    
    clock.tick(fps)

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    if len(snake_list)>snake_length:
        del snake_list[0]
    

    snake_size_change = snake_size +10
    # check_collids(snake_x, snake_y)
    score_show(score_pos_x, score_pos_y)
    plot_snake(window, black,snake_list,snake_size)
    pygame.draw.rect(window,red,[food_x,food_y,food_size,food_size])

    pygame.display.update()