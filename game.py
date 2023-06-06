import settings
import pygame
import gui


class Game:
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        self.walls = []
        self.state = "main menu"
        self.play_button = gui.Button((settings.WIDTH/2, settings.HEIGHT/2, settings.WIDTH/2, settings.HEIGHT/2), settings.GREEN, lambda: self.play_function(), text="PLAY",hover_color=settings.BLACK)
        self.quit_button = gui.Button2((0, settings.HEIGHT/2, settings.WIDTH/2, settings.HEIGHT/2), settings.RED, lambda: self.quit_function(), text="OPTIONS")

    def start(self):
        self.running = True


    def play_function(self):
        self.state = "running"

    def quit_function(self):
        self.state = "options"
        #self.running = False
    def death_screen(self):
        self.state = "death screen"


    def update(self):
        self.clock.tick(settings.FPS)

    def events(self):
        for event in pygame.event.get():
            self.play_button.check_event(event)
            self.quit_button.check_event(event)

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = "main menu"

def draw_text(window, text, size, color, x, y, centered):
    font = pygame.font.Font(settings.FONT, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    if centered:
        text_rect.midtop = (x, y)
    window.blit(text_surface, text_rect)


    # for event in pygame.event.get():
    #
    #     # Close Program on Quit
    #     if event.type == pygame.QUIT:
    #         running = False
    #
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_ESCAPE:
    #             running = False