import pygame
from settings import *
from src.cuerpos import CUERPOS

# CLASE SERPIENTE
class SERPIENTE(pygame.sprite.Sprite):
  def __init__(self, lista_serpiente, lista_comida, lista_global):
    pygame.sprite.Sprite.__init__(self)

    self.lista_serpiente = lista_serpiente
    self.lista_comida = lista_comida
    self.lista_global = lista_global

    self.SONIDO_COMIDA = pygame.mixer.Sound('assets/sound/COMIDA.wav')
    self.SONIDO_COMIDA.set_volume(1.0)

    self.CABEZA = pygame.image.load("assets/images/CABEZA.png").convert_alpha()
    self.image = self.CABEZA

    self.rect = self.image.get_rect()
    self.rect.y = (BALDOSA_NUMERO / 2) * BALDOSA_TAMANIO
    self.rect.x = (BALDOSA_NUMERO / 2) * BALDOSA_TAMANIO

    self.PUNTOS = 0
    self.DIRECCION = 'I'
    self.TERMINA = False

  def AGREGAR_NUEVO_CUERPO(self):
    nuevo_cuerpo = CUERPOS(self.rect.x, self.rect.y)
    self.lista_serpiente.add(nuevo_cuerpo)
    self.lista_global.add(nuevo_cuerpo)

  def update(self):
    COORD_ACTUAL_X = self.rect.x
    COORD_ACTUAL_Y = self.rect.y

    if self.DIRECCION == 'I':
      self.image = pygame.transform.rotate(self.CABEZA, 90)
      self.rect.x -= BALDOSA_TAMANIO
    elif self.DIRECCION == 'D':
      self.image = pygame.transform.rotate(self.CABEZA, -90)
      self.rect.x += BALDOSA_TAMANIO
    elif self.DIRECCION == 'A':
      self.image = pygame.transform.rotate(self.CABEZA, 0)
      self.rect.y -= BALDOSA_TAMANIO
    elif self.DIRECCION == 'B':
      self.image = pygame.transform.rotate(self.CABEZA, 180)
      self.rect.y += BALDOSA_TAMANIO

    for ELT in self.lista_serpiente:
      x = ELT.GET_X()
      y = ELT.GET_Y()
      ELT.set_xy(COORD_ACTUAL_X, COORD_ACTUAL_Y)
      COORD_ACTUAL_X = x
      COORD_ACTUAL_Y = y

    if self.rect.x >= ALTURA:
      self.rect.x = 0
    elif self.rect.x < 0:
      self.rect.x = ALTURA - BALDOSA_TAMANIO
    elif self.rect.y >= ANCHURA:
      self.rect.y = MARCADOR_ANCHURA
    elif self.rect.y < MARCADOR_ANCHURA:
      self.rect.y = ANCHURA - MARCADOR_ANCHURA

    LISTA_COLISION_SERPIENTE = pygame.sprite.spritecollide(self, self.lista_serpiente, False)
    if len(LISTA_COLISION_SERPIENTE):
      print("Perdido")
      self.TERMINA = True

    LISTA_COLISION_COMIDA = pygame.sprite.spritecollide(self, self.lista_comida, False)
    for comida in LISTA_COLISION_COMIDA:
      comida.kill()
      self.AGREGAR_NUEVO_CUERPO()
      self.SONIDO_COMIDA.play()
      self.PUNTOS += PUNTO_UNIDAD