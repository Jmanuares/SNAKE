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

while True:
    #Exit game by clicking the cross
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    #Serpiente movimiento        
        if event.type == SCREEN_UPDATE:
            snake.movimientoSerpiente()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)
            if event.key == pygame.K_SPACE:
                snake.serpienteCrecer()
    if not snake.getRectSerpienteCabeza() is None:
        if snake.getRectSerpienteCabeza().right > bordes or snake.getRectSerpienteCabeza().left < 0:
            pygame.quit()
            sys.exit 
        if snake.getRectSerpienteCabeza().midbottom[1] > bordes or snake.getRectSerpienteCabeza().midtop[1] < 0:
            pygame.quit()
            sys.exit 
    #Draw elements
    pygame.display.update()
    screen.fill((170,200,70))
    fruit.dibujarFruta()
    snake.dibujarSerpiente()
    
    #Limitar 60 Fps
    Clock.tick(60)
    
    