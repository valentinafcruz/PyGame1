import pygame
from os import path

FPS = 60
BLACK = (0, 0, 0)

def game_over_screen(tela, WIDTH, HEIGHT):
    clock = pygame.time.Clock()

    # Carrega imagem de fundo e do botão
    fundo = pygame.image.load(path.join('assets/Game over.jpeg')).convert()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))

    botao = pygame.image.load(path.join('assets/Botão Restart.jpeg')).convert_alpha()
    botao = pygame.transform.scale(botao, (370, 120))
    botao_rect = botao.get_rect(topleft=(190,550))

    # # Define posição do botão (centralizado)
    # botao_x = WIDTH // 2 - 100  # 100 é metade da largura do botão
    # botao_y = HEIGHT // 2 + 100  # Ajuste a altura como quiser

    # # Cria um retângulo para detectar clique
    # botao_rect = pygame.Rect(botao_x, botao_y, 400, 100)

    running = True
    while running:
        tela.blit(fundo, (0, 0))

        # Desenha o botão na tela
        tela.blit(botao, botao_rect)

        pygame.display.update()
        clock.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if botao_rect.collidepoint(mouse_pos):
                    return 0  # Volta para o menu inicial (INIT)