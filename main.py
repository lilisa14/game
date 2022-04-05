import pygame
from gun import Gun
import controls
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("SnenegrBlack")
    bg = pygame.image.load("image/floor.jpg")
    rectf = bg.get_rect()
    gun = Gun(screen)
    bullets = Group()

    while True:
        screen.blit(bg, rectf)
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg, screen, gun, bullets)
        controls.delete(bullets)

run()