from Pantalla import Pantalla
import pygame
import random


pantalla = Pantalla()
Celdas = pantalla.getCeldas()
CeldasTamaño = pantalla.getCeldasTamaño()
screen = pantalla.getScreen()

class Fruit:
    def setPosicion(self,posicion):
        self.posicion = posicion

    def getPosicion(self):
        return None        

    def __init__(self):
        self.x = random.randint(0,Celdas - 1)
        self.y = random.randint(0,Celdas - 1)
        self.pos = pygame.math.Vector2(self.x,self.y)

    def dibujarFruta(self):
        x_pos = int(self.pos.x * CeldasTamaño)
        y_pos = int(self.pos.y * CeldasTamaño)
        rectFruta = pygame.Rect(x_pos,y_pos,CeldasTamaño,CeldasTamaño)
        pygame.draw.rect(screen,(255,0,0),rectFruta)