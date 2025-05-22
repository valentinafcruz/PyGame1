#Mecânica das telas 
import pygame
from init_screen import *
from gameover import *
from jogo import *

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

# ----- Inicializa tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# ----- Inicializa assets

while state != QUIT:
    if state == INIT:
        state = init_screen(screen, WIDTH, HEIGHT)
    if state == FASE1:
        state = fase1(screen, WIDTH, HEIGHT)

    # if state == FASE2:
    #     state = fase2(screen)
    # if state == FASE3:
    #     state = fase3(screen)
    if state == GAMEOVER:
        state = game_over_screen(screen)