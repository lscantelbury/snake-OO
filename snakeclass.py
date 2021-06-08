import pygame

position = [100, 50]
body = [[100, 50],
        [90, 50],
        [80, 50],
        [70, 50]
        ]

class Snake():
    def __init__(self, position, body, speed, direction):
        self.position = position
        self.body = body
        self.speed = speed
        self.direction = direction
    
    
    def snakemovement(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = 'UP'
                if event.key == pygame.K_DOWN:
                    self.direction = 'DOWN'
                if event.key == pygame.K_LEFT:
                    self.direction = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    self.direction = 'RIGHT'

        if self.direction == 'UP':
            snake.position[1] -= 10
        if self.direction == 'DOWN':
            snake.position[1] += 10
        if self.direction == 'LEFT':
            snake.position[0] -= 10
        if self.direction == 'RIGHT':
            snake.position[0] += 10

snake = Snake(position, body, 15, 'RIGHT')