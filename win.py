import pygame
from os import path

FPS = 60
BLACK = (0, 0, 0)

def win_screen(tela, WIDTH, HEIGHT, tempo_final):

    # Carrega a imagem de fundo da tela de vitória
    fundo = pygame.image.load(path.join('assets', 'win_screen.jpeg')).convert()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
    
    font = pygame.font.SysFont(None, 36)
    tempo_surface = font.render(tempo_final, True, (0, 0, 0)) 

    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Se apertar qualquer tecla, volta para a tela inicial
            if evento.type == pygame.KEYDOWN:
                return 0  # Volta para o estado INIT (menu inicial)
        
        tela.blit(fundo, (0, 0))  # Desenha o fundo
        tela.blit(tempo_surface, (400, 400))  # Mostra o tempo final
        pygame.display.update()  # Atualiza a tela
    
    
