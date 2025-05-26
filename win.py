import pygame
from os import path

FPS = 60
BLACK = (0, 0, 0)

def win_screen(tela, WIDTH, HEIGHT):
    clock = pygame.time.Clock()

    # Carrega a imagem de fundo da tela de vitória
    fundo = pygame.image.load(path.join('assets', 'win_screen.jpeg')).convert()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))

    running = True
    while running:
        tela.blit(fundo, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Se apertar qualquer tecla, volta para a tela inicial
            if evento.type == pygame.KEYDOWN:
                return 0  # Volta para o estado INIT (menu inicial)
