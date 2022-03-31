import pygame
from gun import Gun
import controls
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("SnenegrBlack")
    bg_color = (75, 0, 130)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controls.events(screen,gun,bullets)
        gun.update_gun()
        controls.update(bg_color,screen,gun, bullets)
        controls.delete(bullets)

run()