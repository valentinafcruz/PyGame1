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

