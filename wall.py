import settings
import pygame

class Wall:
    def __init__(self):
        self.speed = 100
        self.rectHeight = 400
        self.rectWidth = 400
        self.color = settings.GRAY
        self.y_pos = settings.HEIGHT/2 - self.rectHeight/2
        self.x_pos = settings.WIDTH/2 - self.rectWidth/2


        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.rectWidth, self.rectHeight)

    def update(self):
        pass

        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.rectWidth, self.rectHeight)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)