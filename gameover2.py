import pygame 
from os import path

FPS = 60
BLACK = (0, 0, 0)
GAME = 1
QUIT = 2
GAMEOVER = 3

def game_over_screen(tela, WIDTH, HEIGHT):
    clock = pygame.time.Clock()

    fundo = pygame.image.load(path.join('assets/gameover.jpg')).convert()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))

    running = True
    while running:
        tela.blit(fundo, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return QUIT