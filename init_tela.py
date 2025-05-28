import pygame 
from mapas_das_fases import *
from os import path

INIT = 0
GAME = 1
QUIT = 2
GAMEOVER = 3
FASE1 = 4
FASE2 = 5
FASE3 = 6

def init_screen(tela, WIDTH, HEIGHT):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    fundo = pygame.image.load(path.join('assets/Tela de Inicio.png')).convert()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))

    botao = pygame.image.load(path.join('assets/Botão de Play.png')).convert_alpha()
    botao = pygame.transform.scale(botao, (320, 220))
    botao_rect = botao.get_rect(topleft=(240,605))


    running = True
    while running:
        tela.blit(fundo, (0, 0))
        tela.blit(botao, botao_rect)
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return QUIT
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(evento.pos):
                    return FASE1


