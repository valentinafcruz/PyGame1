# Mecânica das telas 
import pygame
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('FatCatRush')

from init_screen import *
from gameover import *
from funçõesdasfases import *
from classes import *
from win import *




# Música de fundo
pygame.mixer.music.load('som/musica de fundo.mp3')
pygame.mixer.music.play(-1)

# Sons de evento
som_nivel = pygame.mixer.Sound('som/passou de nivel musica.mp3')
som_gameover = pygame.mixer.Sound('som/gameover music.wav')
som_vitoria = pygame.mixer.Sound('som/som_vitoria.wav')
from classes import *

INIT = 0
GAME = 1
QUIT = 2
GAMEOVER = 3
# Fases
FASE1 = 4
FASE2 = 5
FASE3 = 6
WIN  = 7

state = INIT
clock = pygame.time.Clock()
FPS = 30
player = player(gato_imgs)
clock.tick(FPS) 


# ----- Inicializa tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Tempo inicial do cronômetro
crom_tempo = None
# Loop principal
while state != QUIT:
    # ===== CRONÔMETRO =====
    
    # ======================
    
    if state == INIT:
        state = init_screen(screen, WIDTH, HEIGHT)
        crom_tempo = None  # Reseta o cronômetro quando volta para a tela inicial
    if state == FASE1:
        if crom_tempo == None:
            crom_tempo = pygame.time.get_ticks() // 1000  # transforma em segundos        
        state = fase1(screen, WIDTH, HEIGHT, player, crom_tempo)

    if state == FASE2:
        pygame.mixer.music.pause()
        som_nivel.play()
        pygame.time.delay(1000)
        pygame.mixer.music.unpause()
    
        # Atualiza o tempo
        state = fase2(screen, WIDTH, HEIGHT, player, crom_tempo)

    if state == FASE3:
        pygame.mixer.music.pause()
        som_nivel.play()
        pygame.time.delay(1000)
        pygame.mixer.music.unpause()
        state = fase3(screen, WIDTH, HEIGHT, player, crom_tempo)

    if state == WIN:
        pygame.mixer.music.stop()
        som_vitoria.play()
        pygame.time.delay(1000)
        tempo_final = pygame.time.get_ticks() - crom_tempo * 1000  # Tempo total em milissegundos
        minutos = tempo_final // 60000
        segundos = (tempo_final % 60000) // 1000
        tempo_formatado = f"{minutos:02d}:{segundos:02d}"
        state = win_screen(screen, WIDTH, HEIGHT, tempo_formatado)
        pygame.mixer.music.play(-1)
        
    if state == GAMEOVER:
        pygame.mixer.music.stop()
        som_gameover.play()
        pygame.time.delay(1000)
        state = game_over_screen(screen, WIDTH, HEIGHT)
        if state == INIT:
            pygame.mixer.music.play(-1) 
    if state == QUIT:
        pygame.quit()
        exit()
pygame.quit()
exit()

