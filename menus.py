import pygame
import settings
import gui


rect = pygame.Rect(0, 0, settings.WIDTH, settings.HEIGHT / 2)
rect2 = pygame.Rect(0, settings.HEIGHT / 2, settings.WIDTH / 2, settings.HEIGHT / 2)
rect3 = pygame.Rect(settings.WIDTH / 2, settings.HEIGHT / 2, settings.WIDTH / 2, settings.HEIGHT / 2)


def main_menu(window, play_button, quit_button):
    pygame.draw.rect(window, settings.BLUE, rect)
    pygame.draw.rect(window, settings.RED, rect2)
    pygame.draw.rect(window, settings.GREEN, rect3)
    gui.draw_text(window, "Main Menu", settings.FONT_SIZE, settings.BLACK, settings.WIDTH / 2,
                  (settings.HEIGHT / 4) - settings.FONT_SIZE / 2, True)
    gui.draw_text(window, "Quit", settings.FONT_SIZE, settings.BLACK, settings.WIDTH / 4,
                  (settings.HEIGHT / 4 + settings.HEIGHT / 2) - settings.FONT_SIZE / 2, True)
    gui.draw_text(window, "Options", settings.FONT_SIZE, settings.BLACK, settings.WIDTH / 4 + settings.WIDTH / 2,
                  (settings.HEIGHT / 4 + settings.HEIGHT / 2) - settings.FONT_SIZE / 2, True)
    play_button.update(window)
    quit_button.update(window)

def options(window):
    window.fill(settings.LIGHT_BLUE)
    gui.draw_text(window, "Options",int(settings.FONT_SIZE/2), settings.BLACK,settings.WIDTH/2,0, True)

def death_screen(window):
    window.fill(settings.BLACK)
    gui.draw_text(window, "L Bozo", int(settings.FONT_SIZE * 3), settings.RED, settings.WIDTH/2, settings.HEIGHT/2, True)
