#Mecânica das telas 
import pygame
from init_screen import *
from gameover import *
from jogo import *
from classes import *

INIT = 0
GAME = 1
QUIT = 2
GAMEOVER = 3
FASE1 = 4
FASE2 = 5
FASE3 = 6

state = INIT

# Inicializa o pygame
pygame.init()
clock = pygame.time.Clock()
FPS = 30
player = player()
clock.tick(FPS) 


# ----- Inicializa tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# ----- Inicializa assets

while state != QUIT:
    if state == INIT:
        state = init_screen(screen, WIDTH, HEIGHT)
    if state == FASE1:
        state = fase1(screen, WIDTH, HEIGHT, player)
    if state == GAMEOVER:
        state = game_over_screen(screen)
    if state == QUIT:
        pygame.quit()
        exit()
pygame.quit()
exit()