
# importing libraries
import pygame
import time
import random
import snakeclass
import fruit
import test 
import menu

# Window size
window_x = 800
window_y = 600
  
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
  
# Initialising pygame
pygame.init()
  
# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
  
# FPS (frames per second) controller
fps = pygame.time.Clock()

position = [100, 50]
body = [[100, 50],
        [90, 50],
        [80, 50],
        [70, 50]
       ]

snake = snakeclass.Snake(position, body, 15, 'RIGHT', 0, green)

fruit_position = [random.randrange(1, (800//10)) * 10, 
                  random.randrange(1, (600//10)) * 10]
fruit_spawn = True

fruit = fruit.Fruit(fruit_position, fruit_spawn, red)

# inital score
score = 0


# displaying Score function
def show_score(choice, color, font, size):
    
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
      
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
      
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
      
    # displaying text
    game_window.blit(score_surface, score_rect)
  
# game over function
def game_over():
    
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
      
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
      
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
      
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
      
    # blit wil draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
      
    # after 2 seconds we will quit the program
    time.sleep(2)
      
    # deactivating pygame library
    pygame.quit()
      
    # quit the program
    quit()
  
  
# Main Function
while True:
    
    snake.snakemovement()
    snake.snakeProgression()

    # If two keys pressed simultaneously
    # we don't want snake to move into two 
    # directions simultaneously
    '''if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT')'''
  
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake.body.insert(0, list(snake.position))
    if snake.position[0] == fruit.position[0] and snake.position[1] == fruit.position[1]:
        score += 10
        snake.streak += 1
        fruit.spawn = False
    else:
        snake.body.pop()
          
    if not fruit.spawn:
        fruit.position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
          
    fruit.spawn = True
    game_window.fill(black)
      
    for pos in snake.body:
        pygame.draw.rect(game_window, snake.color,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit.position[0], fruit.position[1], 10, 10))
  
    # Game Over conditions
    if snake.position[0] < 0 or snake.position[0] > window_x-10:
        game_over()
    if snake.position[1] < 0 or snake.position[1] > window_y-10:
        game_over()
  
    # Touching the snake body
    for block in snake.body[1:]:
        if snake.position[0] == block[0] and snake.position[1] == block[1]:
            game_over()
  
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)
  
    # Refresh game screen
    pygame.display.update()
  
    # Frame Per Second /Refres Rate
    fps.tick(snake.speed)