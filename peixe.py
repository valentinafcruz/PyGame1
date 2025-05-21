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
gato_img = pygame.image.load("assets/gato_magro_sem.png")
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






import pygame
import sys

# Inicialização
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gato Come Peixes com Armadilhas")
clock = pygame.time.Clock()

# Cores
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Imagens (você pode carregar com pygame.image.load se tiver)
gato_img = pygame.Surface((50, 50))
gato_img.fill((255, 200, 0))

peixe_img = pygame.Surface((30, 30))
peixe_img.fill((0, 200, 255))

# Classe Peixe
class Peixe:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)

    def desenhar(self, tela):
        tela.blit(peixe_img, self.rect.topleft)

    def foi_comido(self, gato_rect):
        return self.rect.colliderect(gato_rect)

# Classe Bloco Mortal
class BlocoMortal:
    def __init__(self, x, y):
        self.x_base = x
        self.y = y
        self.estado = "parede"
        self.timer = 0
        self.rect = pygame.Rect(x, y, 50, 50)

    def atualizar(self, dt):
        self.timer += dt
        if self.estado == "parede" and self.timer >= 2000:
            self.estado = "ataque"
            self.timer = 0
        elif self.estado == "ataque" and self.timer >= 1000:
            self.estado = "parede"
            self.timer = 0

    def get_rect(self):
        if self.estado == "parede":
            return pygame.Rect(self.x_base, self.y, 50, 50)
        else:
            return pygame.Rect(self.x_base + 50, self.y, 50, 50)

    def desenhar(self, tela):
        pygame.draw.rect(tela, RED, self.get_rect())

    def colide_com_gato(self, gato_rect):
        return self.estado == "ataque" and self.get_rect().colliderect(gato_rect)

# Inicializações
gato_x, gato_y = 100, 100
gato_speed = 5
vidas = 3

peixes = [Peixe(200, 200), Peixe(400, 100), Peixe(600, 400)]
blocos = [BlocoMortal(300, 300), BlocoMortal(500, 500)]

# Loop principal
running = True
while running and vidas > 0:
    dt = clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # Movimento do gato
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: gato_x -= gato_speed
    if teclas[pygame.K_RIGHT]: gato_x += gato_speed
    if teclas[pygame.K_UP]: gato_y -= gato_speed
    if teclas[pygame.K_DOWN]: gato_y += gato_speed
    gato_rect = pygame.Rect(gato_x, gato_y, 50, 50)

    # Atualização de blocos e verificação de colisão
    for bloco in blocos:
        bloco.atualizar(dt)
        if bloco.colide_com_gato(gato_rect):
            vidas -= 1
            print("Você perdeu uma vida!")
            gato_x, gato_y = 100, 100
            break

    # Verifica peixes comidos
    peixes = [p for p in peixes if not p.foi_comido(gato_rect)]

    # Desenha tudo
    screen.fill(BLACK)
    screen.blit(gato_img, (gato_x, gato_y))
    for p in peixes: p.desenhar(screen)
    for b in blocos: b.desenhar(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
