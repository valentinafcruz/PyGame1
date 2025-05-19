# import pygame
# import sys

# # Inicialização
# pygame.init()
# WIDTH = 800
# HEIGHT = 800
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Labirinto com Barreiras")

# # Cores
# BLACK = (0, 0, 0)
# PURPLE = (190, 50, 255)

# # Lista para armazenar retângulos das paredes (barreiras)
# barreiras = []

# # Classe Player
# class Player:
#     def __init__(self):
#         self.x = 100
#         self.y = 100
#         self.speed = 8
#         self.image = pygame.image.load('assets/gato_sem_fundo.png').convert_alpha()
#         self.image = pygame.transform.scale(self.image, (40, 40))
#         self.width = 40
#         self.height = 40

#     def move(self, dx, dy):
#         new_rect = pygame.Rect(self.x + dx, self.y + dy, self.width, self.height)
#         if not check_collision(new_rect):
#             self.x += dx
#             self.y += dy

#     def draw(self):
#         window.blit(self.image, (self.x, self.y))

# # Instância do jogador
# player = Player()

# # Função para desenhar o labirinto
# def draw_maze():
#     window.fill(BLACK)
#     wall_thickness = 10

#     def draw_wall(x, y, w, h):
#         rect = pygame.Rect(x, y, w, h)
#         pygame.draw.rect(window, PURPLE, rect)
#         barreiras.append(rect)

#     barreiras.clear()

#     # Paredes - Labirinto 1
#     draw_wall(50, 50, 10, 400)
#     draw_wall(50, 50, 350, 10)
#     draw_wall(390, 50, 10, 400)
#     draw_wall(50, 450, 100, 10)
#     draw_wall(110, 150, 10, 200)
#     draw_wall(110, 140, 150, 10)
#     draw_wall(110, 350, 160, 10)
#     draw_wall(150, 450, 10, 140)
#     draw_wall(50, 590, 110, 10)
#     draw_wall(50, 590, 10, 150)
#     draw_wall(50, 740, 220, 10)
#     draw_wall(270, 350, 10, 400)
#     draw_wall(260, 140, 10, 160)
#     draw_wall(260, 300, 70, 10)
#     draw_wall(320, 300, 10, 300)
#     draw_wall(390, 450, 160, 10)
#     draw_wall(550, 450, 10, 220)
#     draw_wall(320, 600, 160, 10)
#     draw_wall(480, 600, 10, 140)
#     draw_wall(480, 740, 210, 10)
#     draw_wall(550, 670, 50, 10)
#     draw_wall(600, 410, 10, 270)
#     draw_wall(690, 260, 10, 490)
#     draw_wall(460, 410, 150, 10)
#     draw_wall(460, 200, 10, 210)
#     draw_wall(460, 200, 230, 10)
#     draw_wall(690, 50, 10, 160)
#     draw_wall(690, 260, 50, 10)
#     draw_wall(740, 50, 10, 220)
#     draw_wall(690, 50, 50, 10)

# # Função para verificar colisão com barreiras
# def check_collision(new_rect):
#     for wall in barreiras:
#         if new_rect.colliderect(wall):
#             return True
#     return False

# # Desenha o labirinto uma vez
# draw_maze()

# # Loop principal
# clock = pygame.time.Clock()
# FPS = 30
# while True:
#     clock.tick(FPS)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Verifica teclas pressionadas
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         player.move(-player.speed, 0)
#     if keys[pygame.K_RIGHT]:
#         player.move(player.speed, 0)
#     if keys[pygame.K_UP]:
#         player.move(0, -player.speed)
#     if keys[pygame.K_DOWN]:
#         player.move(0, player.speed)

#     # Redesenha tudo
#     draw_maze()
#     player.draw()
#     pygame.display.flip()
# ===== Inicialização =====
# ----- Importa e inicia pacotes
# ===== Inicialização =====
# ----- Importa e inicia pacotes
# ===== Inicialização =====
# ----- Importa e inicia pacotes
# import pygame
# from init_screen import init_screen

# pygame.init()

# # ----- Gera tela principal
# WIDTH = 800
# HEIGHT = 800
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Pygame')


# # ----- Inicia assets
# fundo_img = pygame.display.set_mode((WIDTH, HEIGHT))
# parede = pygame.image.load('assets\maze_pixel_art-removebg-preview.png').convert_alpha()
# parede = pygame.transform.scale(parede, (WIDTH, HEIGHT))
# peixe_img = pygame.image.load("assets/WhatsApp Image 2025-05-14 at 09.56.52.jpeg")
# peixe_img = pygame.transform.scale(peixe_img, (30, 30))

# # Cores
# BLACK = (0, 0, 0)
# PURPLE = (190, 50, 255)

# # ----- Inicia estruturas de dados
# class player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.rect = pygame.Rect(60, 60, 45, 45)
#         self.speedx = 0
#         self.speedy = 0
#         self.image = pygame.image.load('assets/gato_sem_fundo.png').convert_alpha()
#         self.image = pygame.transform.scale(self.image, (50, 50))
    
#     def move(self):

#         new_rect = pygame.Rect(self.rect.x + self.speedx, self.rect.y + self.speedy, self.rect.width, self.rect.height)
#         pygame.draw.rect(window, (255, 0, 0), new_rect)  # Desenha o retângulo temporário para depuração

#         if not check_collision(new_rect):
#             if self.rect.right > WIDTH:
#                 self.rect.right = WIDTH
#                 self.speedx = 0
#             elif self.rect.left < 0:
#                 self.rect.left = 0
#                 self.speedx = 0
#             elif self.rect.bottom > HEIGHT:
#                 self.rect.bottom = HEIGHT
#                 self.speedy = 0
#             elif self.rect.top < 0:
#                 self.rect.top = 0
#                 self.speedy = 0
#             else:
#                 self.rect.x += self.speedx
#                 self.rect.y += self.speedy
#         else:
#             self.speedx = 0
#             self.speedy = 0
        

#     def draw(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# class Peixe:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.rect = pygame.Rect(x, y, 30, 30)

#     def desenhar(self, tela):
#         tela.blit(peixe_img, (self.x, self.y))

#     def foi_comido(self, gato_rect):
#         return self.rect.colliderect(gato_rect)

# # Lista de objetos Peixe
# peixes = [
#     Peixe(70, 70),
#     # Peixe(400, 100),
#     # Peixe(600, 400),
#     # Peixe(50, 120),
#     # Peixe(690, 190),
#     # Peixe(630, 100)
# ]

# # Função para verificar colisão com barreiras
# def check_collision(new_rect):
#     for wall in barreiras:
#         if new_rect.colliderect(wall):
#             return True
#     return False

# # Lista para armazenar retângulos das paredes (barreiras)
# barreiras = []
# # ----- Função para desenhar o labirinto 
# def draw_maze():
#     window.fill(BLACK)

#     def draw_wall(x, y, w, h):
#         rect = pygame.Rect(x, y, w, h)
#         pygame.draw.rect(window, PURPLE, rect)
#         barreiras.append(rect)

#     barreiras.clear()

#     # Paredes - Labirinto 1
#     # draw_wall(0,0,50,800)
#     # draw_wall(100,200,50,600)
#     draw_wall(50, 50, 10, 400)
#     draw_wall(50, 50, 350, 10)
#     draw_wall(390, 50, 10, 400)
#     draw_wall(50, 450, 100, 10)
#     draw_wall(110, 150, 10, 200)
#     draw_wall(110, 140, 150, 10)
#     draw_wall(110, 350, 160, 10)
#     draw_wall(150, 450, 10, 140)
#     draw_wall(50, 590, 110, 10)
#     draw_wall(50, 590, 10, 150)
#     draw_wall(50, 740, 220, 10)
#     draw_wall(270, 350, 10, 400)
#     draw_wall(260, 140, 10, 160)
#     draw_wall(260, 300, 70, 10)
#     draw_wall(320, 300, 10, 300)
#     draw_wall(390, 450, 160, 10)
#     draw_wall(550, 450, 10, 220)
#     draw_wall(320, 600, 160, 10)
#     draw_wall(480, 600, 10, 140)
#     draw_wall(480, 740, 210, 10)
#     draw_wall(550, 670, 50, 10)
#     draw_wall(600, 410, 10, 270)
#     draw_wall(690, 260, 10, 490)
#     draw_wall(460, 410, 150, 10)
#     draw_wall(460, 200, 10, 210)
#     draw_wall(460, 200, 230, 10)
#     draw_wall(690, 50, 10, 160)
#     draw_wall(690, 260, 50, 10)
#     draw_wall(740, 50, 10, 220)
#     draw_wall(690, 50, 50, 10)
# # ===== Loop principal =====

# clock = pygame.time.Clock()
# FPS = 30
# player = player()

# INIT = 0
# GAME = 1
# QUIT = 2
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# state = init_screen(screen, WIDTH, HEIGHT)
# # Inicia o jogo 

# while state != QUIT:
#     clock.tick(FPS)
#     # ----- Trata eventos
#     for event in pygame.event.get():
#         # ----- Verifica consequências
#         if event.type == pygame.QUIT:
#             state = QUIT
#         # Verifica se apertou alguma tecla.
#         if state == GAME:
#             if event.type == pygame.KEYDOWN:
#                 # Dependendo da tecla, altera a velocidade.
#                 if player.speedx == 0 and player.speedy == 0:
#                     if event.key == pygame.K_LEFT:
#                         player.speedx = -10
#                         player.speedy = 0
#                     if event.key == pygame.K_RIGHT:
#                         player.speedx = 10
#                         player.speedy = 0
#                     if event.key == pygame.K_UP:        
#                         player.speedy =- 10
#                         player.speedx = 0
#                     if event.key == pygame.K_DOWN:
#                         player.speedy = 10
#                         player.speedx = 0

#     peixes = [peixe for peixe in peixes if not peixe.foi_comido(gato_rect)]
#     # ----- Gera saídas
#     draw_maze()   # Desenha o labirinto
#     player.move()  # Move o personagem
#     player.draw() # Desenha o personagem
#     pygame.display.update()  # Atualiza a tela

# # ===== Finalização =====
# pygame.quit()  # Função do PyGame que finaliza os recursos utilizados



import pygame
from init_screen import init_screen

pygame.init()

# ----- Gera tela principal
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame')

# ----- Inicia assets
parede = pygame.image.load('assets/maze_pixel_art-removebg-preview.png').convert_alpha()
parede = pygame.transform.scale(parede, (WIDTH, HEIGHT))
peixe_img = pygame.image.load("assets/Peixe sem fundo.png")
peixe_img = pygame.transform.scale(peixe_img, (30, 30))

# Cores
BLACK = (0, 0, 0)
PURPLE = (190, 50, 255)

# Lista para armazenar retângulos das paredes (barreiras)
barreiras = []

# ----- Função para verificar colisão com barreiras
def check_collision(new_rect):
    for wall in barreiras:
        if new_rect.colliderect(wall):
            return True
    return False

# ----- Classe do jogador
def draw_maze():
    window.fill(BLACK)

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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(60, 60, 45, 45)
        self.speedx = 0
        self.speedy = 0
        self.image = pygame.image.load('assets/gato_sem_fundo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

    def move(self):
        new_rect = pygame.Rect(self.rect.x + self.speedx, self.rect.y + self.speedy, self.rect.width, self.rect.height)

        if not check_collision(new_rect):
            if new_rect.right > WIDTH:
                self.rect.right = WIDTH
                self.speedx = 0
            elif new_rect.left < 0:
                self.rect.left = 0
                self.speedx = 0
            elif new_rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
                self.speedy = 0
            elif new_rect.top < 0:
                self.rect.top = 0
                self.speedy = 0
            else:
                self.rect = new_rect
        else:
            self.speedx = 0
            self.speedy = 0

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Peixe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 30, 30)

    def desenhar(self, tela):
        tela.blit(peixe_img, (self.x, self.y))

    def foi_comido(self, gato_rect):
        return self.rect.colliderect(gato_rect)

# Lista de peixes
peixes = [
    Peixe(100, 410),
    # Peixe(80, 410),
    # outros peixes...
]

# ===== Loop principal =====
clock = pygame.time.Clock()
FPS = 30
player = Player()

INIT = 0
GAME = 1
QUIT = 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
state = init_screen(screen, WIDTH, HEIGHT)

while state != QUIT:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = QUIT
        if state == GAME and event.type == pygame.KEYDOWN:
            if player.speedx == 0 and player.speedy == 0:
                if event.key == pygame.K_LEFT:
                    player.speedx = -10
                    player.speedy = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 10
                    player.speedy = 0
                if event.key == pygame.K_UP:
                    player.speedy = -10
                    player.speedx = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 10
                    player.speedx = 0

    # Atualiza lista de peixes (remove os comidos)
    peixes = [peixe for peixe in peixes if not peixe.foi_comido(player.rect)]

    draw_maze()
    player.move()
    player.draw()

    for peixe in peixes:
        peixe.desenhar(window)

    pygame.display.update()

pygame.quit()