from FRUTAS import Celdas
import pygame
from  pygame.math import Vector2
from Pantalla import Pantalla

pantalla = Pantalla()

screen = pantalla.getScreen()
CeldasTamaño = pantalla.getCeldasTamaño()

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.rectSerpiente = None
        self.rectSerpienteCabeza = None
        self.pos = None



    def dibujarSerpiente(self):
        x_pos = int((self.body[0]).x * CeldasTamaño )
        y_pos = int((self.body[0]).y * CeldasTamaño )
        self.pos = pygame.math.Vector2((self.body[0]),(self.body[0]))
        self.rectSerpienteCabeza = pygame.Rect(x_pos,y_pos,CeldasTamaño ,CeldasTamaño )
        for block in self.body:
            x_pos = int(block.x * CeldasTamaño )
            y_pos = int(block.y * CeldasTamaño )
            self.rectSerpiente = pygame.Rect(x_pos,y_pos,CeldasTamaño ,CeldasTamaño )
            pygame.draw.rect(screen,("green"),self.rectSerpiente)
        



    def getCuerpo(self):
        return self.body


    def getPos(self):
        return self.pos
    
    def getRectSerpiente(self):
        return self.rectSerpiente


    def getRectSerpienteCabeza(self):
        return self.rectSerpienteCabeza


    def movimientoSerpiente(self):
        cuerpo = self.body[:-1]
        cuerpo.insert(0,cuerpo[0] + self.direction)
        self.body = cuerpo[:]
    
    def serpienteCrecer(self):
        cuerpo = self.body[:]
        cuerpo.insert(0,cuerpo[0] + self.direction)
        self.body = cuerpo[:]
    


    
        