import pygame
import sys
from FRUTAS import Fruit
from SNAKE import Snake
from Pantalla import Pantalla
from  pygame.math import Vector2

#init
pygame.init()


# Resolucion y Pantalla
pantalla = Pantalla()
screen = pantalla.getScreen()
bordes = pantalla.getBordes()


snake = Snake()
fruit = Fruit()

#FPS
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
Clock = pygame.time.Clock()

#texto
fuente = pygame.font.Font(None, 30)

#player
score = 0

#Fruta
RectFruta = None

#Serpiente
def serpiente():
    snake.dibujarSerpiente()
CabezaSerp = None
CuerpoSerp = None

while True:
    
    Puntaje = fuente.render(f"Puntaje = {score}",None,"red")

    #Make rect
    CabezaSerp = snake.getRectSerpienteCabeza()
    RectFruta = fruit.getRectFruta()
    CuerpoSerp = snake.getRectSerpiente()
    
    #Exit game by clicking the cross
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    #Serpiente movimiento        
        if event.type == SCREEN_UPDATE:
            snake.movimientoSerpiente()
            for block in snake.getCuerpo()[2:]:
                if snake.getPos() == pygame.math.Vector2((block),(block)):
                    pygame.quit()
                    sys.exit 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)

    #Colision de serpiente
    if fruit.getpos() == snake.getPos():   
            fruit = Fruit()
            snake.serpienteCrecer()
            fruit.dibujarFruta()
            score += 1

    if not CabezaSerp is None:
        if CabezaSerp.right > bordes or CabezaSerp.left < 0:
            pygame.quit()
            sys.exit 
        if CabezaSerp.midbottom[1] > bordes or CabezaSerp.midtop[1] < 0:
            pygame.quit()
            sys.exit 

    
        


    #Draw elements
    pygame.display.update()
    screen.fill((170,200,70))
    screen.blit(Puntaje,(10,10))
    fruit.dibujarFruta()
    serpiente()
    #Limitar 60 Fps
    Clock.tick(60)
    
    