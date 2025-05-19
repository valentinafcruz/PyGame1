import pygame 
from os import path


# from jogo import IMG_DIR, BLACK, FPS, GAME, QUIT
FPS = 60
BLACK = (0, 0, 0)
GAME = 1
QUIT = 0

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
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(evento.pos):
                    return GAME
                    running = False


