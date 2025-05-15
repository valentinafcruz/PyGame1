import pygame
import sys

# Inicialização
pygame.init()
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirinto com Barreiras")

# Cores
BLACK = (0, 0, 0)
PURPLE = (190, 50, 255)

# Lista para armazenar retângulos das paredes (barreiras)
barreiras = []

# Classe Player
class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 8
        self.image = pygame.image.load('assets/gato_sem_fundo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.width = 40
        self.height = 40

    def move(self, dx, dy):
        new_rect = pygame.Rect(self.x + dx, self.y + dy, self.width, self.height)
        if not check_collision(new_rect):
            self.x += dx
            self.y += dy

    def draw(self):
        window.blit(self.image, (self.x, self.y))

# Instância do jogador
player = Player()

# Função para desenhar o labirinto
def draw_maze():
    window.fill(BLACK)
    wall_thickness = 10

    def draw_wall(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(window, PURPLE, rect)
        barreiras.append(rect)

    barreiras.clear()

    # Paredes - Labirinto 1
    draw_wall(50, 50, 10, 400)
    draw_wall(50, 50, 350, 10)
    draw_wall(390, 50, 10, 400)
    draw_wall(50, 450, 100, 10)
    draw_wall(110, 150, 10, 200)
    draw_wall(110, 140, 150, 10)
    draw_wall(110, 350, 160, 10)
    draw_wall(150, 450, 10, 140)
    draw_wall(50, 590, 110, 10)
    draw_wall(50, 590, 10, 150)
    draw_wall(50, 740, 220, 10)
    draw_wall(270, 350, 10, 400)
    draw_wall(260, 140, 10, 160)
    draw_wall(260, 300, 70, 10)
    draw_wall(320, 300, 10, 300)
    draw_wall(390, 450, 160, 10)
    draw_wall(550, 450, 10, 220)
    draw_wall(320, 600, 160, 10)
    draw_wall(480, 600, 10, 140)
    draw_wall(480, 740, 210, 10)
    draw_wall(550, 670, 50, 10)
    draw_wall(600, 410, 10, 270)
    draw_wall(690, 260, 10, 490)
    draw_wall(460, 410, 150, 10)
    draw_wall(460, 200, 10, 210)
    draw_wall(460, 200, 230, 10)
    draw_wall(690, 50, 10, 160)
    draw_wall(690, 260, 50, 10)
    draw_wall(740, 50, 10, 220)
    draw_wall(690, 50, 50, 10)

# Função para verificar colisão com barreiras
def check_collision(new_rect):
    for wall in barreiras:
        if new_rect.colliderect(wall):
            return True
    return False

# Desenha o labirinto uma vez
draw_maze()

# Loop principal
clock = pygame.time.Clock()
FPS = 30
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Verifica teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-player.speed, 0)
    if keys[pygame.K_RIGHT]:
        player.move(player.speed, 0)
    if keys[pygame.K_UP]:
        player.move(0, -player.speed)
    if keys[pygame.K_DOWN]:
        player.move(0, player.speed)

    # Redesenha tudo
    draw_maze()
    player.draw()
    pygame.display.flip()
