import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Tela
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gato Come Peixes")

# Clock
clock = pygame.time.Clock()

# Imagens
gato_img = pygame.image.load("assets/gato_sem_fundo.png")
gato_img = pygame.transform.scale(gato_img, (50, 50))

peixe_img = pygame.image.load("assets/WhatsApp Image 2025-05-14 at 09.56.52.jpeg")
peixe_img = pygame.transform.scale(peixe_img, (30, 30))

# Classe do Peixe
class Peixe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 30, 30)

    def desenhar(self, tela):
        tela.blit(peixe_img, (self.x, self.y))

    def foi_comido(self, gato_rect):
        return self.rect.colliderect(gato_rect)

# Lista de objetos Peixe
peixes = [
    Peixe(200, 200),
    Peixe(400, 100),
    Peixe(600, 400),
    Peixe(50, 120),
    Peixe(690, 190),
    Peixe(630, 100)
]

# Posição do Gato
gato_x, gato_y = 100, 100
gato_speed = 5

# Função para desenhar tudo
def desenhar_tela():
    screen.fill((0, 0, 0))  # Fundo preto
    screen.blit(gato_img, (gato_x, gato_y))

    for peixe in peixes:
        peixe.desenhar(screen)

    pygame.display.flip()

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do gato
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        gato_x -= gato_speed
    if teclas[pygame.K_RIGHT]:
        gato_x += gato_speed
    if teclas[pygame.K_UP]:
        gato_y -= gato_speed
    if teclas[pygame.K_DOWN]:
        gato_y += gato_speed

    gato_rect = pygame.Rect(gato_x, gato_y, 50, 50)

    # Verifica colisões e remove peixes comidos
    peixes = [peixe for peixe in peixes if not peixe.foi_comido(gato_rect)]

    desenhar_tela()
    clock.tick(60)

pygame.quit()
sys.exit()
