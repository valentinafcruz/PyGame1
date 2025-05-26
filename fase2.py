import pygame
import sys

# Inicializa o pygame
pygame.init()

# Tamanho da janela
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mapa Level2 - Visualização")

# Cor das paredes
BLACK = (255, 255, 255)
WHITE  = (0, 0, 0)
WALL_COLOR = (0, 255, 0)

# Lista para armazenar as barreiras (opcional, se quiser detectar colisões depois)
barreiras = []

# Função para desenhar paredes
def draw_wall1(x, y, width, height):
    pygame.draw.rect(screen, WALL_COLOR, (x, y, width, height))
    barreiras.append(pygame.Rect(x, y, width, height))

# Função que desenha o labirinto
def mapa_level2():
    barreiras.clear()
    
    # Cantos
    draw_wall1(0, 0, 50, 800)     # Parede esquerda
    draw_wall1(0, 0, 800, 50)     # Parede superior
    draw_wall1(0, 750, 800, 50)   # Parede inferior
    draw_wall1(750, 0, 50, 800)   # Parede direita

    # Labirinto interno
    draw_wall1(100, 600, 50, 150)      # 1
    draw_wall1(50, 500, 400, 50)      # 2
    draw_wall1(250, 200, 50, 500)     # 3
    draw_wall1(350, 600, 50, 300)      # 4
    draw_wall1(400, 600, 50, 500)     # 5
    draw_wall1(500, 600, 200, 100)      # 6
    draw_wall1(550, 400, 50, 200)     # 7
    draw_wall1(500, 300, 50, 150)    # 8
    draw_wall1(250, 300, 300, 50)     # 9
    draw_wall1(700, 500, 50, 50)     # 10
    draw_wall1(600, 400, 50, 250)      # 11
    draw_wall1(650, 400, 50, 50)     # 12
    draw_wall1(600, 300, 150, 50)      # 13
    draw_wall1(450, 50, 50, 200)     # 14
    # draw_wall1(550, 100, 50, 50)     # 15
    draw_wall1(400, 200, 50, 50)      # 16
    draw_wall1(250, 50, 50, 100)      # 17
    draw_wall1(200, 250, 50, 50)
    draw_wall1(50, 350, 50, 50)
