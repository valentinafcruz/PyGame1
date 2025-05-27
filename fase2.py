import pygame

BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)

def mapa_level2(screen):
    barreiras = []
    screen.fill(BLACK)

    def paredes(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, YELLOW, rect)
        barreiras.append(rect)

    # Paredes da fase 2
    paredes(0,0,50,800)
    paredes(0,0,800,50)
    paredes(0,750,800,50)
    paredes(750,0,50,800)

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

def check_collision(nova_posicao, barreiras):
    for wall in barreiras:
        if nova_posicao.colliderect(wall):
            return True
    return False
# import pygame
# import sys
# # Inicializa o pygame
# pygame.init()

# # Tamanho da janela
# WIDTH, HEIGHT = 800, 800
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Mapa Level2 - Visualização")

# # Cor das paredes
# BLACK = (0, 0, 0)
# YELLOW = (255,215,0)
# WHITE  = (0, 0, 0)


# # Função para verificar colisão com barreiras
# def check_collision(nova_posicao):
#     for wall in barreiras:
#         if nova_posicao.colliderect(wall):
#             return True
#     return False 

# def paredes(x, y, w, h):
#         rect = pygame.Rect(x, y, w, h)
#         pygame.draw.rect(screen, YELLOW, rect)
#         barreiras.append(rect)

# # Lista para armazenar as barreiras (opcional, se quiser detectar colisões depois)
# barreiras = []

# # Função para desenhar paredes
# def mapa_level2():

#     barreiras.clear()

#     # pygame.draw.rect(screen, YELLOW, (x, y, width, height))
#     # barreiras.append(pygame.Rect(x, y, width, height))

#     paredes(0,0,50,800)
#     paredes(0,0,800,50)
#     paredes(0,750,800,50)
#     paredes(750,0,50,800)
    
#     paredes(50,100,150,50) #1
#     paredes(250,50,50,600) #2
#     paredes(100, 200, 150, 50) #3
#     paredes(50, 300, 150, 50) #4
#     paredes(100, 450, 150, 50) #5
#     paredes(50, 600, 150, 50) #6
#     paredes(300, 700, 500, 500) #8
#     paredes(300, 600, 300, 50) #9
#     paredes(350, 450, 300, 50) #10
#     paredes(600, 500, 50, 50) #11
#     paredes(300, 250, 300, 50) #12
#     paredes(300, 300, 50, 50) #13
#     paredes(450, 350, 50, 100) #14
#     paredes(350, 100, 300, 50) #15
#     paredes(600, 150, 50, 50) #16
#     paredes(650,100, 50, 700) #7
