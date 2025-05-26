# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from inimigo import *     
from classes import *
from fase1 import *
from fase2 import *

pygame.init()

# ----- Gera tela principal

INIT = 0
GAME = 1
QUIT = 2
GAMEOVER = 3
FASE1 = 4
FASE2 = 5
FASE3 = 6
WIN = 7

# ===== Loop principal =====

def fase1(screen, WIDTH, HEIGHT, player):
    #Define a posição inicial do player
    player.rect.x = 50
    player.rect.y = 50  
    # Lista de peixes1
    peixes1 = [
    Peixe(100, 410),        
    Peixe(60, 410),
    Peixe(200, 410),
    Peixe(300, 410),
  
    # escrever outros peixes1...
    ]
    # ----- Grupos de sprites
    grupo_inimigos1 = pygame.sprite.Group()
    grupo_tiros_inimigos1 = pygame.sprite.Group()

    inimigo1 = Inimigo(300, 90, 'baixo')
    grupo_inimigos1.add(inimigo1)
    
    state = FASE1
    # Inicia o jogo 
    while state != QUIT and state != GAMEOVER:
        mapa_level1() # Desenha o labirinto
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                return QUIT
            # Verifica se apertou alguma tecla.
            if state == FASE1:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade
                    if player.speedx == 0 and player.speedy == 0:
                        if event.key == pygame.K_LEFT:
                            player.speedx = -5
                            player.speedy = 0
                        if event.key == pygame.K_RIGHT:
                            player.speedx = 5
                            player.speedy = 0
                        if event.key == pygame.K_UP:        
                            player.speedy =- 5
                            player.speedx = 0
                        if event.key == pygame.K_DOWN:
                            player.speedy = 5
                            player.speedx = 0

            # Atualiza lista de peixes1 (remove os comidos)
        peixes1 = [peixe for peixe in peixes1 if not peixe.foi_comido(player.rect)]

        for peixe in peixes1:
            peixe.desenhar(window)

            # ----- Gera saídas

        player.move()  # Move o personagem
        player.draw() # Desenha o personagem
        pygame.display.update()  # Atualiza a tela
        
        if len(peixes1) == 0:
            return 5  # WIN
            
    return state

def fase2(screen, WIDTH, HEIGHT, player):
    # ----- Define posição inicial do player
    player.rect.x = 50
    player.rect.y = 50  
    
    # ----- Grupos de sprites
    grupo_inimigos = pygame.sprite.Group()
    grupo_tiros_inimigos = pygame.sprite.Group()

    # ----- Cria inimigos
    inimigo1 = Inimigo(300, 90, 'baixo')
    inimigo2 = Inimigo(600, 220, 'direita')
    inimigo3 = Inimigo(235, 370, 'esquerda')
    grupo_inimigos.add(inimigo1, inimigo2, inimigo3)

    # ----- Lista de peixes
    peixes = [
        Peixe(100, 410),        
        Peixe(60, 410),
        Peixe(200, 410),
        Peixe(300, 410),
        Peixe(500, 500),
    ]

    state = FASE2

    # Loop da fase
    while state != QUIT and state != GAMEOVER:
        screen.fill((0, 0, 0))  # Limpa a tela
        mapa_level2()  # Desenha o labirinto

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if player.speedx == 0 and player.speedy == 0:
                    if event.key == pygame.K_LEFT:
                        player.speedx = -5
                        player.speedy = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 5
                        player.speedy = 0
                    if event.key == pygame.K_UP:
                        player.speedy = -5
                        player.speedx = 0
                    if event.key == pygame.K_DOWN:
                        player.speedy = 5
                        player.speedx = 0

        # Atualiza inimigos (corrigido)
        grupo_inimigos.update(grupo_tiros_inimigos)

        # Desenha peixes restantes
        peixes = [peixe for peixe in peixes if not peixe.foi_comido(player.rect)]
        for peixe in peixes:
            peixe.desenhar(screen)

        # Desenha inimigos
        grupo_inimigos.draw(screen)

        # Move e desenha o jogador
        player.move()
        player.draw()

        pygame.display.update()

        # Condição para passar de fase (exemplo: pegou todos os peixes)
        if len(peixes) == 0:
            return FASE3

    return state
