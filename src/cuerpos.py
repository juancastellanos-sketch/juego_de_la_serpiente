import pygame
#from settings import RUTA_CUERPOS


class CUERPOS(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/images/CUERPO.png").convert_alpha()
        self.rect  = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def GET_X(self):
        return self.rect.x

    def GET_Y(self):
        return self.rect.y

    def set_xy(self, x, y):
        self.rect.x = x
        self.rect.y = y