import pygame

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
purple = pygame.Color(128, 0, 128)
green = pygame.Color(8, 186, 2)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
snakeColorProgression = [yellow, blue, purple]

class Snake():
    def __init__(self, position, body, speed, direction, streak, color):
        self.position = position
        self.body = body
        self.speed = speed
        self.direction = direction
        self.streak = streak
        self.color = color
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
                if event.key == pygame.K_SPACE:
                    self.speed += 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.speed -= 10

        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'RIGHT':
            self.position[0] += 10
    
    def snakeProgression(self):

        if self.streak == 5:
            self.color = snakeColorProgression[0]
            self.speed = 20

        if self.streak == 10:
            self.color = snakeColorProgression[1]
            self.speed = 25

        if self.streak == 20:
            self.color = snakeColorProgression[2]
            self.speed = 30

        if self.streak > 24:
            self.color = green
            self.speed = 15

