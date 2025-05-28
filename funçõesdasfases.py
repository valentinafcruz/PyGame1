# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame    
from classes import *
from funções import * 
from mapas_das_fases import *

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

def fase1(screen, WIDTH, HEIGHT, player, tempo_inicial):
    #Define a posição inicial do player
    player.nivel = 0  # Gato magro
    player.rect.x = 50
    player.rect.y = 700
    font = pygame.font.SysFont(None, 36)
    
    # Lista de peixes1
    peixes1 = [
    Peixe(160, 360),
    Peixe(110, 360),        
    Peixe(60, 410),
    Peixe(210, 360),
    Peixe(60, 360),        
    Peixe(60, 310),
    Peixe(60, 260),
    Peixe(60, 310),
    Peixe(60, 610),        
    Peixe(60, 660),
    Peixe(110, 610),
    Peixe(110, 710),
    Peixe(160, 610),

    Peixe(160, 710),
    Peixe(210, 710),
    Peixe(210, 660),        
    Peixe(210, 610),
    Peixe(210, 560),
    Peixe(210, 510),
    Peixe(210, 460),
    Peixe(210, 410),

    Peixe(60, 210),
    Peixe(60, 160),
    Peixe(60, 110),        
    Peixe(60, 60),
    Peixe(110, 60),
    Peixe(160, 60),
    Peixe(210, 60),
    Peixe(260, 60),
    Peixe(310, 60),
    Peixe(360, 60),

    Peixe(360, 110),
    Peixe(310, 110),
    Peixe(260, 110),
    Peixe(260, 160),
    Peixe(260, 210),
    Peixe(260, 260),

    Peixe(310, 160),
    Peixe(310, 210),
    Peixe(310, 260),
    Peixe(310, 310),
    Peixe(310, 360),
    Peixe(310, 410),
    Peixe(310, 460),
    Peixe(310, 510),
    Peixe(310, 560),

    Peixe(360, 210),
    Peixe(360, 260),
    Peixe(360, 310),
    Peixe(360, 360),
    Peixe(360, 410),
    Peixe(360, 460),
    Peixe(360, 510),
    Peixe(360, 560),

    Peixe(410, 460),
    Peixe(410, 560),
    Peixe(460, 460),
    Peixe(460, 560),
    Peixe(510, 460),
    Peixe(510, 510),
    Peixe(510, 560),

    Peixe(510, 610),
    Peixe(510, 660),
    Peixe(510, 710),
    Peixe(560, 710),
    Peixe(610, 710),

    Peixe(610, 660),
    Peixe(610, 610),
    Peixe(610, 560),
    Peixe(610, 510),
    Peixe(610, 460),
    Peixe(610, 410),
    Peixe(610, 360),
    Peixe(610, 310),
    Peixe(610, 260),
    Peixe(610, 210),

    Peixe(660, 660),
    Peixe(660, 610),
    Peixe(660, 560),
    Peixe(660, 510),
    Peixe(660, 460),
    Peixe(660, 410),
    Peixe(660, 360),
    Peixe(660, 310),
    Peixe(660, 260),
    Peixe(660, 210),

    Peixe(560, 360),
    Peixe(560, 210),

    Peixe(510, 360),
    Peixe(510, 210),

    Peixe(460, 360),
    Peixe(460, 310),
    Peixe(460, 260),
    Peixe(460, 210),

    Peixe(710, 210),
    Peixe(710, 160),
    Peixe(710, 110),
    Peixe(710, 60),
    ]
    
    state = FASE1
    # Inicia o jogo 
    while state != QUIT and state != GAMEOVER:
        barreiras = mapa_level1(screen) # Desenha o labirinto
        #tempo
        tempo_atual = pygame.time.get_ticks() - tempo_inicial
        minutos = tempo_atual // 60000
        segundos = (tempo_atual % 60000) // 1000
        tempo_format = f"{minutos:02}:{segundos:02}"  # Formata o tempo como MM:SS
        tempo_surface = font.render(tempo_format, True, (0, 0, 0))  # Atualiza a superfície do tempo    
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
        
        if check_collision(player.rect.move(player.speedx, player.speedy), barreiras):
            player.speedx = 0
            player.speedy = 0

            # Atualiza lista de peixes1 (remove os comidos)
        peixes1 = [peixe for peixe in peixes1 if not peixe.foi_comido(player.rect)]

        for peixe in peixes1:
            peixe.desenhar(screen)

            # ----- Gera saídas

        player.move(barreiras)  # Move o personagem
        player.draw(screen) # Desenha o personagem
        screen.blit(tempo_surface, (0, 0))  # Desenha o tempo na tela
        pygame.display.update()  # Atualiza a tela
        
        if len(peixes1) == 0:
            return 5  # WIN
            
    return state

def fase2(screen, WIDTH, HEIGHT, player, tempo_inicial):
    # ----- Define posição inicial do player
    player.nivel = 1 # Gato médio
    player.rect.x = 50
    player.rect.y = 50  
    
    font = pygame.font.SysFont(None, 36)
      
    # ----- Grupos de sprites
    grupo_inimigos = pygame.sprite.Group()
    grupo_tiros_inimigos = pygame.sprite.Group()

    # ----- Cria inimigos
    inimigo1 = Inimigo(70, 375, 'baixo') 
    inimigo2 = Inimigo(70, 675, 'direita')
    inimigo3 = Inimigo(230, 525, 'esquerda')
    inimigo4 = Inimigo(580, 525, 'baixo') 
    inimigo7 = Inimigo(540, 525, 'esquerda') 
    inimigo5 = Inimigo(369, 325, 'direita')
    inimigo6 = Inimigo(580, 175, 'esquerda')
    # inimigo8 = Inimigo(520, 425, 'direita')
    grupo_inimigos.add(inimigo1, inimigo2, inimigo3, inimigo4, inimigo5, inimigo6, inimigo7)

    # ----- Lista de peixes
    peixes = peixes = [
        Peixe(110, 410),        
        Peixe(60, 410),
        Peixe(160, 410),
        Peixe(210, 410),
        Peixe(210, 360),
        Peixe(210, 310),
        Peixe(210, 260),

        Peixe(110, 260),        
        Peixe(60, 260),
        Peixe(160, 260),

        Peixe(60, 210),
        Peixe(60, 160),
        Peixe(110, 160),
        Peixe(160, 160),
        Peixe(210, 160),

        Peixe(210, 110),        
        Peixe(210, 60),
        Peixe(160, 60),
        Peixe(110, 60),        
        
        Peixe(60, 460),
        Peixe(60, 510),
        Peixe(60, 560),
        Peixe(110, 560),
        Peixe(160, 560),
        Peixe(210, 610),
        Peixe(210, 560),
        Peixe(210, 660),
        Peixe(210, 710),
        Peixe(60, 710),
        Peixe(110, 710),
        Peixe(160, 710),
        Peixe(260, 710),

        Peixe(260, 660),
        Peixe(310, 660), 
        Peixe(360, 660),
        Peixe(410, 660), 
        Peixe(460, 660),
        Peixe(510, 660), 
        Peixe(560, 660),
        Peixe(510, 660),
        Peixe(560, 660),

        Peixe(610, 660),
        Peixe(610, 610), 
        Peixe(610, 560),
        Peixe(560, 560), 
        Peixe(510, 560),
        Peixe(460, 560), 
        Peixe(410, 560),
        Peixe(360, 560),
        Peixe(310, 560),

        Peixe(310, 510),
        Peixe(310, 460), 
        Peixe(310, 410),
        Peixe(310, 360), 
        Peixe(360, 360),
        Peixe(410, 360), 
        Peixe(410, 410),
        Peixe(360, 410),
        Peixe(410, 310),

        Peixe(460, 310),
        Peixe(510, 310), 
        Peixe(560, 310),
        Peixe(610, 310), 
        Peixe(610, 360),
        Peixe(610, 410), 
        Peixe(510, 410),
        Peixe(510, 360),
        Peixe(560, 410),
        

        Peixe(610, 260),
        Peixe(560, 210), 
        Peixe(510, 210),
        Peixe(610, 210), 
        Peixe(460, 210),
        Peixe(410, 210), 
        Peixe(360, 210),
        Peixe(310, 210),
        Peixe(310, 160),
        Peixe(310, 110),
        Peixe(310, 60),

        Peixe(360, 60), 
        Peixe(410, 60), 
        Peixe(460, 60),
        Peixe(510, 60), 
        Peixe(560, 60), 
        Peixe(610, 60), 
        Peixe(660, 60),
        Peixe(710, 60), 
        Peixe(710, 110),
        Peixe(710, 160),
        Peixe(710, 210),
        Peixe(710, 260),
        Peixe(710, 310),
        Peixe(710, 360),
        Peixe(710, 410),
        Peixe(710, 460),
        Peixe(710, 510),
        Peixe(710, 560),
        Peixe(710, 610),
        Peixe(710, 660),
     ]


    state = FASE2

    # Loop da fase
    while state != QUIT and state != GAMEOVER:
        screen.fill((0, 0, 0))  # Limpa a tela
        barreiras = mapa_level2(screen)  # Desenha o labirinto
        # Atualiza o tempo
        tempo_atual = pygame.time.get_ticks() - tempo_inicial
        minutos = tempo_atual // 60000
        segundos = (tempo_atual % 60000) // 1000
        tempo_format = f"{minutos:02}:{segundos:02}"  # Formata o tempo como MM:SS
        tempo_surface = font.render(tempo_format, True, (0, 0, 0))  # Atualiza a superfície do tempo   
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
        if check_collision(player.rect.move(player.speedx, player.speedy), barreiras):
            player.speedx = 0
            player.speedy = 0
        if pygame.sprite.spritecollideany(player, grupo_inimigos):
            return GAMEOVER
        if pygame.sprite.spritecollideany(player, grupo_tiros_inimigos):
            return GAMEOVER

        # Atualiza inimigos (corrigido)
        grupo_inimigos.update(grupo_tiros_inimigos)
        grupo_tiros_inimigos.update(barreiras)
        grupo_tiros_inimigos.draw(screen)

        # Desenha peixes restantes
        peixes = [peixe for peixe in peixes if not peixe.foi_comido(player.rect)]
        for peixe in peixes:
            peixe.desenhar(screen)

        # Desenha inimigos
        grupo_inimigos.draw(screen)

        # Move e desenha o jogador
        player.move(barreiras)
        player.draw(screen)
        screen.blit(tempo_surface, (0, 0))  # Desenha o tempo na tela
        pygame.display.update()

        # Condição para passar de fase (exemplo: pegou todos os peixes)
        if len(peixes) == 0:
            return FASE3
    return state

def fase3(screen, WIDTH, HEIGHT, player, tempo_inicial):
    # ----- Define posição inicial do player
    player.nivel = 2  # Gato gordo
    player.rect.x = 50
    player.rect.y = 700  
    
    font = pygame.font.SysFont(None, 36)
    
    # ----- Grupos de sprites
    grupo_inimigos = pygame.sprite.Group()
    grupo_tiros_inimigos = pygame.sprite.Group()

    # ----- Cria inimigos
    inimigo1 = Inimigo(170, 725, 'cima')#inicio
    inimigo2 = Inimigo(675, 220, 'baixo')#meio superior direita
    inimigo3 = Inimigo(625, 180, 'esquerda')#meio superior direita
    inimigo4 = Inimigo(675, 180, 'direita')#meio superior direita
    inimigo5 = Inimigo(625, 220, 'baixo')#meio superior direita
    inimigo6 = Inimigo(675, 140, 'direita')#meio superior direita
    inimigo7 = Inimigo(625, 140, 'esquerda')#meio superior direita
    inimigo8 = Inimigo(380, 425, 'cima')#meio
    inimigo9 = Inimigo(420, 425, 'baixo')#meio
    inimigo10 = Inimigo(520, 75, 'direita')
    inimigo11 = Inimigo(375, 125, 'baixo')
    inimigo12 = Inimigo(225, 225, 'cima')
    inimigo13 = Inimigo(120, 375, 'direita')
    grupo_inimigos.add(inimigo1, inimigo2, inimigo3, inimigo4, inimigo5, inimigo6, inimigo7, inimigo8, inimigo9, inimigo10,inimigo11, inimigo12, inimigo13)

    # ----- Lista de peixes
    peixes = [Peixe(60, 660), 
    Peixe(60, 610), 
    Peixe(60, 560),  
    Peixe(110, 560), 
    Peixe(160, 560), 
    Peixe(210, 560), 
    Peixe(210, 610), 
    Peixe(210, 660), 
    Peixe(210, 710),

    Peixe(260, 710), 
    Peixe(310, 710), 
    Peixe(310, 660), 
    Peixe(310, 610), 
    Peixe(310, 560),

    Peixe(360, 560), 
    Peixe(410, 560), 
    Peixe(460, 560),  
    Peixe(510, 560), 
    Peixe(510, 510), 
    Peixe(510, 460), 
    Peixe(460, 460), 
    Peixe(410, 460), 
    Peixe(360, 460),
    Peixe(310, 460), 
    Peixe(310, 410), 
    Peixe(310, 360), 

    Peixe(360, 360), 
    Peixe(410, 360), 
    Peixe(460, 360),  
    Peixe(460, 410), 
    Peixe(460, 510), 
    Peixe(460, 610), 
    Peixe(460, 660), 
    Peixe(460, 710), 
    Peixe(510, 710),
    Peixe(560, 710), 
    Peixe(610, 710), 
    Peixe(660, 710), 
    Peixe(710, 710),

    Peixe(710, 660), 
    Peixe(710, 610), 
    Peixe(710, 560), 
    Peixe(660, 510),
    Peixe(710, 660), 
    Peixe(660, 460), 
    Peixe(710, 460), 
    Peixe(660, 560),

    Peixe(710, 410), 
    Peixe(710, 360), 
    Peixe(660, 360), 
    Peixe(610, 360),
    Peixe(560, 360), 
    Peixe(560, 310), 
    Peixe(560, 260), 
    Peixe(560, 210),
    Peixe(560, 160), 
    Peixe(560, 110), 
    Peixe(560, 60), 
    Peixe(610, 60),
    Peixe(660, 60), 
    Peixe(710, 60), 
    Peixe(710, 110), 
    Peixe(710, 210),
    Peixe(710, 160), 
    Peixe(710, 260), 
    Peixe(660, 260), 
    Peixe(610, 260),

    Peixe(510, 260), 
    Peixe(460, 260), 
    Peixe(410, 260), 
    Peixe(360, 260),
    Peixe(310, 260), 
    Peixe(310, 210), 
    Peixe(310, 160), 
    Peixe(310, 110),
    Peixe(310, 60),  
    Peixe(360, 60), 
    Peixe(410, 60),
    Peixe(410, 110), 
    Peixe(410, 160), 
    Peixe(360, 160), 
    Peixe(260, 160),
    Peixe(210, 160), 
    Peixe(160, 160), 
    Peixe(110, 160), 
    Peixe(60, 160),

    Peixe(60, 60), 
    Peixe(60, 110), 
    Peixe(110, 60), 
    Peixe(160, 60),
    Peixe(210, 60), 
    # Peixe(210, 110), 
    # Peixe(210, 210), 
    # Peixe(310, 110),
    Peixe(310, 60),  
    Peixe(310, 60), 
    Peixe(310, 160),
    Peixe(60, 210), 
    #Peixe(110, 210), 
    #Peixe(160, 210), 
    Peixe(60, 260),
    Peixe(60, 310), 
    Peixe(110, 310), 
    Peixe(160, 310), 
    Peixe(210, 310),

    Peixe(210, 360), 
    Peixe(210, 410), 
    Peixe(210, 460),
    Peixe(160, 460), 
    Peixe(110, 460), 
    Peixe(60, 460),
    Peixe(60, 410),
    ]

    state = FASE3

    # Loop da fase
    while state != QUIT and state != GAMEOVER:
        screen.fill((0, 0, 0))  # Limpa a tela
        barreiras = mapa_level3(screen)   # Desenha o labirinto
        # Atualiza o tempo
        tempo_atual = pygame.time.get_ticks() - tempo_inicial
        minutos = tempo_atual // 60000
        segundos = (tempo_atual % 60000) // 1000
        tempo_format = f"{minutos:02}:{segundos:02}"  # Formata o tempo como MM:SS
        tempo_surface = font.render(tempo_format, True, (0, 0, 0))  # Atualiza a superfície do tempo   
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
        if check_collision(player.rect.move(player.speedx, player.speedy), barreiras):
            player.speedx = 0
            player.speedy = 0
        # Atualiza inimigos (corrigido)
        if pygame.sprite.spritecollideany(player, grupo_inimigos):
            return GAMEOVER
        if pygame.sprite.spritecollideany(player, grupo_tiros_inimigos):
            return GAMEOVER

        # Atualiza inimigos (corrigido)
        grupo_inimigos.update(grupo_tiros_inimigos)
        grupo_tiros_inimigos.update(barreiras)
        grupo_tiros_inimigos.draw(screen)

        # Desenha peixes restantes
        peixes = [peixe for peixe in peixes if not peixe.foi_comido(player.rect)]
        for peixe in peixes:
            peixe.desenhar(screen)

        # Desenha inimigos
        grupo_inimigos.draw(screen)

        # Move e desenha o jogador
        player.move(barreiras)
        player.draw(screen)
        screen.blit(tempo_surface, (0, 0))  # Desenha o tempo na tela
        pygame.display.update()

        # Condição para passar de fase (exemplo: pegou todos os peixes)
        if len(peixes) == 0:
            return WIN

    return state
