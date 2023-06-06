import settings
import pygame
import random
import wall

wall = wall.Wall()
class Enemy:
    def __init__(self, wall):
        self.speed = 1
        self.rectHeight = 100
        self.rectWidth = 100
        self.color = settings.RED
        self.x_pos = random.randint(0, settings.WIDTH - self.rectWidth)
        self.y_pos = random.randint(0, settings.HEIGHT - self.rectHeight)
        self.y_pos = 400
        self.x_pos = 400
        self.wall = wall
        self.enemy_image = pygame.image.load("gigadirectorypictures/Dollarstorechad.png").convert_alpha()
        self.rect = self.enemy_image.get_rect(center = (1, 1))

    def update(self, player):
        self.enemy_movement(player)
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.rectWidth, self.rectHeight)
        self.check_boundary()

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.check_boundary()

        if self.rect.colliderect(self.wall.rect):
            if dy < 0:
                self.rect.top = self.wall.rect.bottom
            if dy > 0:
                self.rect.bottom = self.wall.rect.top
            if dx < 0:
                self.rect.left = self.wall.rect.right
            if dx > 0:
                self.rect.right = self.wall.rect.left

    def check_boundary(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > settings.HEIGHT - self.rectHeight:
            self.rect.y = settings.HEIGHT - self.rectHeight
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > settings.WIDTH - self.rectWidth:
            self.rect.x = settings.WIDTH - self.rectWidth






    def enemy_movement(self, player):
        if not player.rect.colliderect(self.rect):
                if player.rect.x < self.x_pos:
                    self.x_pos -= self.speed

                if player.rect.x > self.x_pos:
                    self.x_pos += self.speed

                if player.rect.y > self.y_pos:
                    self.y_pos += self.speed

                if player.rect.y < self.y_pos:
                    self.y_pos -= self.speed

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)