
# importing libraries
import pygame
import time
import random
import snakeclass
import fruit

# Window size
window_x = 800
window_y = 600

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(219, 70, 15)
green = pygame.Color(8, 186, 2)
blue = pygame.Color(131, 203, 230)
purple = pygame.Color(144, 18, 163)
yellow = pygame.Color(255, 255, 0)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
bg = pygame.image.load('snakebg.png')
game_window.blit(bg, (0, 0))
pygame.display.flip()

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

fruit = fruit.Fruit(fruit_position, fruit_spawn, yellow, 10)

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
def gameover():
    
    # creating font object font
    font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = font.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit wil draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                pass
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()

while True:
    
    snake.snakemovement()
    snake.snakeProgression()


    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake.body.insert(0, list(snake.position))
    if snake.position[0] == fruit.position[0] and snake.position[1] == fruit.position[1]:
        score += fruit.value
        snake.streak += 1
        fruit.changecolor()
        fruit.spawn = False
    else:
        snake.body.pop()
        
    if not fruit.spawn:
        fruit.position = [random.randrange(1, (window_x//10)) * 10, 
                        random.randrange(1, (window_y//10)) * 10]
        
    fruit.spawn = True
    game_window.blit(bg, (0, 0))
    
    for pos in snake.body:
        pygame.draw.rect(game_window, snake.color,
                        pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, fruit.color, pygame.Rect(
        fruit.position[0], fruit.position[1], 10, 10))

    # Game Over conditions
    if snake.position[0] < 0 or snake.position[0] > window_x-10:
        gameover()
    if snake.position[1] < 0 or snake.position[1] > window_y-10:
        gameover()

    # Touching the snake body
    for block in snake.body[1:]:
        if snake.position[0] == block[0] and snake.position[1] == block[1]:
            gameover()

    # displaying score countinuously
    show_score(1, black, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refres Rate
    fps.tick(snake.speed)
