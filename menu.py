import pygame
import time

pygame.init()

class Menu():
    def __init__(self, x, y):
         self.x = x
         self.y = y

    def menuwindow(self):
        pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption(('Snake Menu'))

class Start():
    def __init__(self, x, y, font, color, text):
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.text = text
        
    def drawstart(self):
        starttext = self.font.render(self.text, True, self.color)
        rect = starttext.get_rect()
        Menu.self.blit(rect, (self.x, self.y))
        Menu.pygame.display.flip()

window = Menu(800, 600)

buttonfont = pygame.font.SysFont('times new roman', 20)
startbutton = Start(400, 300, buttonfont, (255,255,255), 'Start')

window.menuwindow()
startbutton.drawstart()

time.sleep(5)

pygame.quit()

quit()