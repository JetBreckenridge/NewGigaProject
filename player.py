import settings
import pygame
import random

class Player:
    def __init__(self, wall):
        self.speed = 10
        self.rectHeight = 100
        self.rectWidth = 100
        self.color = settings.BLUE
        self.wall = wall
        self.max_health = 100
        self.current_health = self.max_health
        self.player_image = pygame.image.load("gigadirectorypictures/gigachad.jpg").convert_alpha()
        self.rect = self.player_image.get_rect()

    def update(self, enemy):
        self.keyboard_movement()
        self.check_collision(enemy)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        self.draw_health_bar(window,0,0,settings.WIDTH/2, settings.WIDTH/20)

    def keyboard_movement(self):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = self.speed

        self.move(dx, dy)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

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

    def check_collision(self,enemy):
        if self.rect.colliderect(enemy.rect):
            self.current_health -= 25
            enemy.x_pos = random.randint(0, settings.WIDTH - enemy.rectWidth)
            enemy.y_pos = random.randint(0, settings.HEIGHT - enemy.rectHeight)

    def draw_health_bar(self,window,x,y,width,height):
        color = settings.RED
        percentage = self.current_health / self.max_health
        if percentage < 0:
            percentage = 0
        filled = percentage * width
        outline_rect = pygame.Rect(x,y,width,height)
        filled_rect = pygame.Rect(x,y, filled,height)
        pygame.draw.rect(window,settings.BLACK,outline_rect)
        pygame.draw.rect(window, color, filled_rect)
        pygame.draw.rect(window, settings.WHITE, outline_rect, 2)


