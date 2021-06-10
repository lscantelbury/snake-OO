import random
import pygame

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(219, 70, 15)
green = pygame.Color(8, 186, 2)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(144, 18, 163)

colorlist = [white, white, white, white, white, red, red, red, blue, blue, purple]

class Fruit():

    def __init__(self, position, spawn, color, value):
        self.position = position
        self.spawn = spawn
        self.color = color
        self.value = value

    def changecolor(self):
        self.color = colorlist[random.randrange(len(colorlist))]
        if self.color == colorlist[0]:
            self.value = 10
        if self.color == colorlist[5]:
            self.value = 15
        if self.color == colorlist[8]:
            self.value = 20
        if self.color == colorlist[10]:
            self.value = 50
       