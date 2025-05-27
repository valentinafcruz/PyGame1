import pygame
from os import path

FPS = 60
BLACK = (0, 0, 0)

def win_screen(tela, WIDTH, HEIGHT, tempo_final):
    clock = pygame.time.Clock()

    # Carrega a imagem de fundo da tela de vitória
    fundo = pygame.image.load(path.join('assets', 'win_screen.jpeg')).convert()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
    
    font = pygame.font.SysFont(None, 48)
    mensagem = f"Tempo: {tempo_final}"
    texto = font.render(mensagem, True, (0, 0, 0))
    tela.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2))

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
    
    
