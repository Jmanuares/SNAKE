import pygame
import random


class Fruit: 
    def __init__(self,CuerpoSerp,Celdas):
        self.y = random.randint(0,Celdas - 2)
        self.x = random.randint(0, Celdas - 2)
        self.rectFruta = None
        self.pos = pygame.math.Vector2(self.x,self.y)
        
        for block in CuerpoSerp:
            
            while self.x == int(block[0]) or self.y == int(block[1]):
                if self.x == block.x:
                    self.x = random.randint(0, Celdas - 2)
                if self.y == block.y:
                    self.y = random.randint(0,Celdas - 2)
    

    def getpos(self):
        return self.pos


    def getRectFruta(self):
        return self.rectFruta


    def dibujarFruta(self,screen,CeldasTamaño):
        x_pos = int(self.pos.x * CeldasTamaño)
        y_pos = int(self.pos.y * CeldasTamaño)
        rectFruta = pygame.Rect(x_pos,y_pos,CeldasTamaño,CeldasTamaño)
        pygame.draw.rect(screen,("red"),rectFruta)