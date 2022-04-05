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


    res = (1000, 600)
    screen = pygame.display.set_mode(res)

    color = (0, 0, 0)
    color_light = (196,114,195)
    color_dark = (176,87,174)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('go', True, color)

    while True:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    while True:
                        screen.blit(bg, rectf)
                        controls.events(screen, gun, bullets)
                        gun.update_gun()
                        controls.update(bg, screen, gun, bullets)
                        controls.delete(bullets)

        screen.fill((85,47,102))

        mouse = pygame.mouse.get_pos()
        if width / 2 -85 <= mouse[0] <= width / 2 +55 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 2 -85, height / 2, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2 -85, height / 2, 140, 40])
        screen.blit(text, (width / 2 - 33, height / 2))
        pygame.display.update()


run()