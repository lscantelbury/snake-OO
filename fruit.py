import random

fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

class Fruit():
    def __init__(self, position, spawn, color):
        self.position = position
        self.spawn = spawn
        self.color = color
    def drawfruit():
        
fruit = Fruit(fruit_position, fruit_spawn )