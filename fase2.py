import pygame
import sys

# Inicializa o pygame
pygame.init()

# Tamanho da janela
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mapa Level2 - Visualização")

# Cor das paredes
BLACK = (0, 0, 0)
YELLOW = (255,215,0)

BLACK = (255, 255, 255)
WHITE  = (0, 0, 0)


# Função para verificar colisão com barreiras
def check_collision(nova_posicao):
    for wall in barreiras:
        if nova_posicao.colliderect(wall):
            return True
    return False 

def paredes(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, YELLOW, rect)
        barreiras.append(rect)

# Lista para armazenar as barreiras (opcional, se quiser detectar colisões depois)
barreiras = []

# Função para desenhar paredes
def draw_wall1(x, y, width, height):
    pygame.draw.rect(screen, YELLOW, (x, y, width, height))
    barreiras.append(pygame.Rect(x, y, width, height))

# Função que desenha o labirinto
def mapa_level2():
    barreiras.clear()
    
    #Paredes - Labirinto 2
    #cantos
    draw_wall1(0,0,50,800)
    draw_wall1(0,0,800,50)
    draw_wall1(0,750,800,50)
    draw_wall1(750,0,50,800)
    
    draw_wall1(50,100,150,50) #1
    draw_wall1(250,50,50,600) #2
    draw_wall1(100, 200, 150, 50) #3
    draw_wall1(50, 300, 150, 50) #4
    draw_wall1(100, 450, 150, 50) #5
    draw_wall1(50, 600, 150, 50) #6
    draw_wall1(300, 700, 500, 500) #8
    draw_wall1(300, 600, 300, 50) #9
    draw_wall1(350, 450, 300, 50) #10
    draw_wall1(600, 500, 50, 50) #11
    draw_wall1(300, 250, 300, 50) #12
    draw_wall1(300, 300, 50, 50) #13
    draw_wall1(450, 350, 50, 100) #14
    draw_wall1(350, 100, 300, 50) #15
    draw_wall1(600, 150, 50, 50) #16
    draw_wall1(650,100, 50, 700) #7
