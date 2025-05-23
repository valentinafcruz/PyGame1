# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from inimigo import Inimigo, TiroInimigo      
from classes import player, Peixe
from funções import *

pygame.init()

# ----- Gera tela principal
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FatCatRush')


# ----- Inicia assets
#fundo_img = pygame.display.set_mode((WIDTH, HEIGHT))
peixe_img = pygame.image.load("assets/peixe_sem_fundo.png").convert_alpha()
peixe_img = pygame.transform.scale(peixe_img, (30, 30))

# Cores
BLACK = (0, 0, 0)
YELLOW = (255,215,0)

INIT = 0
GAME = 1
QUIT = 2
GAMEOVER = 3
FASE1 = 4
FASE2 = 5
FASE3 = 6

# ===== Loop principal =====

clock = pygame.time.Clock()
FPS = 30
player = player()

def fase1(screen, WIDTH, HEIGHT):
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
    # ----- Cria inimigos
    inimigo1 = Inimigo(300, 90, 'baixo')
    inimigo2 = Inimigo(600, 220, 'direita')
    inimigo3 = Inimigo(235, 370, 'esquerda')
    grupo_inimigos1.add(inimigo1, inimigo2, inimigo3)
    state = FASE1
    # Inicia o jogo 
    while state != QUIT:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            # Verifica se apertou alguma tecla.
            if state == GAME:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
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
        if state == GAMEOVER:
            game_over_screen(screen, WIDTH, HEIGHT)
                
        if state == GAME:
            # ----- Atualizações
            grupo_inimigos1.update(grupo_tiros_inimigos1)
            grupo_tiros_inimigos1.update(barreiras)

            # Verifica colisão dos tiros com o player
            if pygame.sprite.spritecollide(player, grupo_tiros_inimigos1):
                state = GAMEOVER
            if pygame.sprite.spritecollide(player, grupo_inimigos1, False):
                state = GAMEOVER

            grupo_inimigos1.draw(screen)
            grupo_tiros_inimigos1.draw(screen)

        # Atualiza lista de peixes1 (remove os comidos)
        peixes1 = [peixe for peixe in peixes1 if not peixe.foi_comido(player.rect)]

        for peixe in peixes1:
            peixe.desenhar(window)

        # ----- Gera saídas
        player.move()  # Move o personagem
        player.draw() # Desenha o personagem
        pygame.display.update()  # Atualiza a tela
        labirinto1() # Desenha o labirinto
