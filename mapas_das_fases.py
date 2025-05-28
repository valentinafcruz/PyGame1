# Fase 1 - Mapa do Labirinto
# Importa as bibliotecas necessárias
import pygame
from funções import *

# Cores utilizadas
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)

def mapa_level1(screen):
    barreiras = []
    screen.fill(BLACK)
    # Função que desenha as paredes do labirinto
    def paredes(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, YELLOW, rect)
        barreiras.append(rect)

    # Construção do labirinto - Fase 1
    # Bordas do labirinto
    paredes(0, 0, 50, 800)     # Parede esquerda
    paredes(0, 0, 800, 50)     # Parede superior
    paredes(0, 750, 800, 50)   # Parede inferior
    paredes(750, 0, 50, 800)   # Parede direita
    # Labirinto interno
    paredes(100,100,50,250)
    paredes(50,450,100,150)
    paredes(100,100,150,250)
    paredes(250,300,50,500)
    paredes(300,600,200,150)
    paredes(400,0,300,200)
    paredes(400,200,50,250)
    paredes(400,400,200,50)
    paredes(550,400,50,300)
    paredes(700,250,50,550)
    paredes(350,150,50,50)
    paredes(650,700,50,50)

    return barreiras

def mapa_level2(screen):
    barreiras = []
    screen.fill(BLACK)
    # Função que desenha as paredes do labirinto
    def paredes(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, YELLOW, rect)
        barreiras.append(rect)

    # Construção do labirinto - Fase 2
    # Bordas do labirinto
    paredes(0, 0, 50, 800)     # Parede esquerda
    paredes(0, 0, 800, 50)     # Parede superior
    paredes(0, 750, 800, 50)   # Parede inferior
    paredes(750, 0, 50, 800)   # Parede direita
    # Labirinto interno
    paredes(50,100,150,50)
    paredes(250,50,50,600)
    paredes(100,200,150,50)
    paredes(50,300,150,50)
    paredes(100,450,150,50)
    paredes(50,600,150,50)
    paredes(300,700,500,500)
    paredes(300,600,300,50)
    paredes(350,450,300,50)
    paredes(600,500,50,50)
    paredes(300,250,300,50)
    paredes(300,300,50,50)
    paredes(450,350,50,100)
    paredes(350,100,300,50)
    paredes(600,150,50,50)
    paredes(650,100,50,700)

    return barreiras

def mapa_level3(screen):
    barreiras = []
    screen.fill(BLACK)
    # Função que desenha as paredes do labirinto
    def paredes(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, YELLOW, rect)
        barreiras.append(rect)
    
    # Bordas do labirinto
    paredes(0, 0, 50, 800)     # Parede esquerda
    paredes(0, 0, 800, 50)     # Parede superior
    paredes(0, 750, 800, 50)   # Parede inferior
    paredes(750, 0, 50, 800)   # Parede direita

    # Labirinto interno
    paredes(100, 600, 50, 150)      
    paredes(50, 500, 400, 50)      
    paredes(250, 200, 50, 500)     
    paredes(350, 600, 50, 300)      
    paredes(400, 600, 50, 500)     
    paredes(500, 600, 200, 100)      
    paredes(550, 400, 50, 200)    
    paredes(500, 300, 50, 150)  
    paredes(250, 300, 300, 50)    
    paredes(700, 500, 50, 50)    
    paredes(600, 400, 50, 250)      
    paredes(650, 400, 50, 50)    
    paredes(600, 300, 150, 50)     
    paredes(450, 50, 50, 200)       
    paredes(400, 200, 50, 50)      
    paredes(250, 50, 50, 100)     
    paredes(200, 250, 50, 50)
    paredes(50, 350, 50, 50)
    
    return barreiras