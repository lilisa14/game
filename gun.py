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

        # self.eimage = pygame.image.load('image/2.png')  # second character
        # self.erect = self.image.get_rect()
        # self.ecenterx = self.screen_rect.centerx
        # self.ebottom = self.screen_rect.bottom
        # self.eright = False
        # self.eleft = False
        # self.eup = False
        # self.edown = False


    def output(self):
        self.screen.blit(self.image, self.rect)
        # self.screen.blit(self.eimage, self.erect)

    def update_gun(self):
        if self.kright and self.rect.right<self.screen_rect.right:
            self.rect.centerx += 1
        if self.kleft == True and self.rect.left>0:
            self.rect.centerx -= 1
        if self.kup == True and self.rect.height<600:
            self.rect.bottom -= 1
        if self.kdown == True and self.rect.bottom<self.screen_rect.bottom:
            self.rect.bottom += 1

    # def update(self):
    #     if self.eright and self.erect.right < self.screen_rect.right+225:
    #         self.erect.centerx += 1
    #     if self.eleft and self.erect.left > -10:
    #         self.erect.centerx -= 1
    #     if self.eup:
    #         self.erect.bottom -= 1
    #     if self.edown:
    #         self.erect.bottom += 1