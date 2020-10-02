import pygame
import random
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

#Initialize Pygame
pygame.init()

#Color Variables
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#Display Width and Height
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height)) #Sets the display
pygame.display.set_caption('Snake Game') #Sets the Caption

clock = pygame.time.Clock() #Clock Variable

#Font Shades
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#function to display SCORE
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

#function to display SNAKE
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


#Funtion to display MESSAGE on Screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#MAIN Function
def gameLoop():
    #Game Variables
    game_over = False
    game_close = False


    snake_block = 10
    snake_speed = 8

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0  # velocity in x
    y1_change = 0  # velocity in y

    snake_List = []
    Length_of_snake = 1 #Initial Length of snake

    score = 0 #Initial Score

    #Variables for Food
    foodx = round(random.randrange(100, dis_width - 100) / 10.0) * 10.0
    foody = round(random.randrange(100, dis_height - 100) / 10.0) * 10.0

    #Main Loop
    while not game_over:

        #After Game gets over
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # q for quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # c for continue
                        gameLoop()

        #For any event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # when snake goes out of the screen
            game_close = True
        x1 += x1_change  # changing position of snake after key press
        y1 += y1_change  # changing position of snake after key press

        if x1 == foodx and y1 == foody:  # when snake eats the food
            score += 10
            foodx = round(random.randrange(100, dis_width - 100) / 10.0) * 10.0
            foody = round(random.randrange(100, dis_height - 100) / 10.0) * 10.0
            Length_of_snake += 1
            if score % 50 == 0:  # increasing speed after every score of 50
                snake_speed += 3
        dis.fill(blue)
        Your_score(score)  # updating the score
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #Drawing the food
        pygame.display.update()

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)


        if len(snake_List) > Length_of_snake:  # cutting the head of snake
            del snake_List[0]

        for x in snake_List[:-1]:  # if snake collides with itself
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop() #Calling the main loop