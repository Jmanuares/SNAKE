import pygame
import sys
from Pantalla import Pantalla
from pygame.math import Vector2
from FRUTAS import Fruit
from SNAKE import Snake
from Player import Player

#init
pygame.init()


# Resolucion y Pantalla
pantalla = Pantalla()
screen = pantalla.getScreen()
bordes = pantalla.getBordes()
CeldasTamaño = pantalla.getCeldasTamaño()
Celdas = pantalla.getCeldas()

#FPS
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
Clock = pygame.time.Clock()

#texto
fuente = pygame.font.Font(None, 30)

#player
player = Player()



#Serpiente
snake = Snake()

#Fruta
RectFruta = None
fruit = Fruit(snake.getCuerpo(),pantalla.getCeldas())





while True:


    #Eventos
    for event in pygame.event.get():

        #Salir del juego con la cruz
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
        

        #Colisiones serpiente
 
        #Morir si se choca con si misma
        for block in snake.getCuerpo()[2:]:
                if snake.getPos() == pygame.math.Vector2((block),(block)):
                    snake = Snake()
                    fruit = Fruit(snake.getCuerpo(),pantalla.getCeldas())
                    if score > highscore:
                        player.sethighscore(score)
                    player.setscore(0)
        
        #Comer fruta
        if fruit.getpos() == snake.getPos():   
                fruit = Fruit(snake.getCuerpo(),pantalla.getCeldas())
                snake.serpienteCrecer()
                player.sumarPuntos()
                
        #Chocarse contra los bordes
        if not snake.getRectSerpienteCabeza() is None:
            CabezaSerp = snake.getRectSerpienteCabeza()

            #borde derecho e izquierdo
            if CabezaSerp.right > bordes or CabezaSerp.left < 0:
                snake = Snake()
                fruit = Fruit(snake.getCuerpo(),pantalla.getCeldas())
                if score > highscore:
                    player.sethighscore(score)
                player.setscore(0)

                #borde arriba o abajo
            if CabezaSerp.midbottom[1] > bordes or CabezaSerp.midtop[1] < 0:
                snake = Snake()
                fruit = Fruit(snake.getCuerpo(),pantalla.getCeldas())
                if score > highscore:
                    player.sethighscore(score)
                player.setscore(0)

    #Score
    score = player.getscore()
    highscore = player.gethighscore()
    Puntaje = fuente.render(f"Score = {int(score)}",None,"Blue")
    maxPuntaje = fuente.render(f"Highscore = {int(highscore)}",None,"Blue")

    #Make rect
    RectFruta = fruit.getRectFruta()
    
    

    
    #Dibujar elementos
    pygame.display.update()
    screen.fill((170,200,70))
    screen.blit(Puntaje,(10,10))
    screen.blit(maxPuntaje,((bordes-(bordes // 2)),10))
    fruit.dibujarFruta(screen,CeldasTamaño)
    snake.dibujarSerpiente(screen,CeldasTamaño)

    #Limitar 60 Fps
    Clock.tick(60)
    
    