# # # FUNÇÕES E VARIÁVEIS
import pygame

WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FatCatRush')
# Cores
BLACK = (0, 0, 0)
YELLOW = (255,215,0)

# Função para verificar colisão com barreiras
def check_collision(nova_posicao):
    for wall in barreiras:
        if nova_posicao.colliderect(wall):
            return True
    return False

def paredes(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(window, YELLOW, rect)
        barreiras.append(rect)

# Lista para armazenar retângulos das paredes (barreiras)
barreiras = []
# ----- Função para desenhar o labirinto 
def labirinto1():
    window.fill(BLACK)
    barreiras.clear()
    #Paredes - Labirinto 1
    #cantos
    paredes(0,0,50,800)
    paredes(0,0,800,50)
    paredes(0,750,800,50)
    paredes(750,0,50,800)
    #resto das paredes
    paredes(100,100,50,250)
    paredes(50, 450, 100, 150)
    paredes(100, 100, 150, 250)
    paredes(250, 300, 50, 500)
    paredes(300, 600, 200, 150)
    paredes(400, 0, 300, 200)
    paredes(400, 200, 50, 250)
    paredes(400, 400, 200, 50)
    paredes(550, 400, 50, 300)
    paredes(700, 250, 50, 550)
    paredes(350, 150, 50, 50)
    paredes(650, 700, 50, 50)

    # def draw_wall2(x, y, w, h):
    #     rect = pygame.Rect(x, y, w, h)
    #     pygame.draw.rect(window, BLACK, rect)
    #     barreiras.append(rect)

    # #moldura
    # draw_wall2(0, 0, 40, 780)
    # draw_wall2(0, 0, 780, 40)
    # draw_wall2(0, 760, 780, 40)
    # draw_wall2(760, 0, 40, 780)

    # # resto das paredes
    # draw_wall2(110, 110, 30, 230)
    # draw_wall2(60, 460, 80, 130)
    # draw_wall2(110, 110, 130, 230)
    # draw_wall2(260, 310, 30, 480)
    # draw_wall2(310, 610, 180, 130)
    # draw_wall2(410, 10, 280, 180)
    # draw_wall2(410, 210, 30, 230)
    # draw_wall2(410, 410, 180, 30)
    # draw_wall2(560, 410, 30, 280)
    # draw_wall2(710, 260, 30, 530)
    # draw_wall2(360, 160, 30, 30)
    # draw_wall2(660, 710, 30, 30)
def labirinto2():
    window.fill(BLACK)
    barreiras.clear()