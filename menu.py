import pygame


class Image(pygame.sprite.Sprite):
    def __init__(self, image, **rect_args):
        super().__init__()
        self.image = pygame.image.load(image) if type(image) is str else image
        self.rect = self.image.get_rect(**rect_args)


class Text(Image):
    def __init__(self, text, font, color=(255, 255, 255), **rect_args):
        self.text = text
        image = font.render(text, False, color)
        super().__init__(image, **rect_args)


class Button(Text):
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and \
            self.rect.collidepoint(pygame.mouse.get_pos())


class MainMenu(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        title_font = pygame.font.SysFont('times new roman', 90)
        button_font = pygame.font.SysFont('times new roman', 50)

        self.bg = Image('snakebg.png')

        self.title = Text('Snake', title_font, center=(400, 100))

        self.start_button = Button("Start", button_font, center=(400, 250))
        self.credits_button = Button("Credits", button_font, center=(400, 350))
        self.quit_button = Button("Quit", button_font, center=(400, 450))

        self.add(self.bg,
                 self.title,
                 self.start_button,
                 self.credits_button,
                 self.quit_button)


# Testing...
if __name__ == '__main__':
    pygame.init()

    menu = MainMenu()

    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    done = False

    while not done:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True

        if menu.start_button.is_clicked():
            print('start')
        elif menu.credits_button.is_clicked():
            print('credits')
        elif menu.quit_button.is_clicked():
            print('quit')
            done = True

        menu.draw(screen)
        pygame.display.flip()

    pygame.quit()
    exit()
