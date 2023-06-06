import player
import pygame
import settings
import enemy
import wall
import game
import menus


pygame.init()
# Set Up A Window
window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)


# enemycolor = settings.BROWN
game = game.Game()
wall = wall.Wall()
player = player.Player(wall)
enemy = enemy.Enemy(wall)


game.start()
# MAIN LOOP
while game.running:
    game.update()
    player.update(enemy)
    game.events()
    enemy.update(player)

    window.fill(settings.WHITE)

    if game.state == "main menu":
        menus.main_menu(window, game.play_button, game.quit_button)
    elif game.state == "options":
        menus.options(window)
    elif game.state == "death screen":
        menus.death_screen(window)

    else:
        player.draw(window)
        window.blit(player.player_image, player.rect)

        enemy.draw(window)
        window.blit(enemy.enemy_image, enemy.rect)

        wall.draw(window)


    pygame.display.update()
