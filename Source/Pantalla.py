import pygame

class Pantalla():
  def __init__(self):
    self.Celdas = 20
    self.CeldasTamaño = 20
    self.Bordes = (self.CeldasTamaño * self.Celdas)

  def getCeldas(self):
      return self.Celdas

  def getCeldasTamaño(self):
      return self.CeldasTamaño

  def getBordes(self):
      return self.Bordes

  def getScreen(self):
    screen = pygame.display.set_mode((self.Bordes, self.Bordes))
    return screen