# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from inimigo import *     
from classes import *
from funções_variáveis import *

pygame.init()

# ----- Gera tela principal

INIT = 0
GAME = 1
QUIT = 2
GAMEOVER = 3
FASE1 = 4
FASE2 = 5
FASE3 = 6

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
    state = FASE1
    # Inicia o jogo 
    while state != QUIT and state != GAMEOVER:
        labirinto1() # Desenha o labirinto
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
                            player.speedx = -25
                            player.speedy = 0
                        if event.key == pygame.K_RIGHT:
                            player.speedx = 25
                            player.speedy = 0
                        if event.key == pygame.K_UP:        
                            player.speedy =- 25
                            player.speedx = 0
                        if event.key == pygame.K_DOWN:
                            player.speedy = 25
                            player.speedx = 0

            # Atualiza lista de peixes1 (remove os comidos)
            peixes1 = [peixe for peixe in peixes1 if not peixe.foi_comido(player.rect)]

            for peixe in peixes1:
                peixe.desenhar(window)

            # ----- Gera saídas

            player.move()  # Move o personagem
            player.draw() # Desenha o personagem
            pygame.display.update()  # Atualiza a tela
            
    return state

# FASE 2
def fase2(screen, WIDTH, HEIGHT, player):
    # ----- Grupos de sprites
    grupo_inimigos1 = pygame.sprite.Group()
    grupo_tiros_inimigos1 = pygame.sprite.Group()
    # ----- Cria inimigos
    inimigo1 = Inimigo(300, 90, 'baixo')
    inimigo2 = Inimigo(600, 220, 'direita')
    inimigo3 = Inimigo(235, 370, 'esquerda')
    grupo_inimigos1.add(inimigo1, inimigo2, inimigo3)