import pygame


class Gun():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.kright = False
        self.kleft = False
        self.kup = False
        self.kdown = False


    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        if self.kright and self.rect.right<self.screen_rect.right:
            self.rect.centerx += 1
        if self.kleft == True and self.rect.left>0:
            self.rect.centerx -= 1
        if self.kup == True and self.rect.height<600:
            self.rect.bottom -= 1
        if self.kdown == True and self.rect.bottom<self.screen_rect.bottom:
            self.rect.bottom += 1
