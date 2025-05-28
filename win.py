import pygame
from os import path

FPS = 60
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)

def win_screen(tela, WIDTH, HEIGHT, tempo_final):

    # Carrega a imagem de fundo da tela de vitória
    fundo = pygame.image.load(path.join('assets', 'win_screen.jpeg')).convert()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
    
    font = pygame.font.SysFont(None, 48)
    texto_tempo = font.render (f"Tempo total:", True, (0, 0, 0))
    num_tempo = font.render(f"{tempo_final}", True, (0, 0, 0))

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
        pygame.draw.rect(tela, YELLOW, (600, 600, 200, 100), 200)  # Desenha um retângulo preto ao redor da tela
        tela.blit(texto_tempo, (600, 600))
        tela.blit(num_tempo, (600, 650))
        pygame.display.update()  # Atualiza a tela
    
    
