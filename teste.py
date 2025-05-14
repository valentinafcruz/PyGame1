import pygame
import sys

# Inicialização
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirinto com Barreiras")

# Cores
BLACK = (0, 0, 0)
PURPLE = (190, 50, 255)
YELLOW = (255, 255, 0)

# Jogador
player_size = 20
player_pos = [100, 100]
player_speed = 4

# Lista para armazenar retângulos das paredes (barreiras)
barreiras = []

# Função para desenhar o labirinto
def draw_maze():
    screen.fill(BLACK)
    wall_thickness = 10

    # Cada parede será adicionada também à lista de barreiras
    def draw_wall(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, PURPLE, rect)
        barreiras.append(rect)

    barreiras.clear()

    # Desenha as paredes simulando o labirinto da imagem
# Desenha as paredes simulando o labirinto da imagem fornecida
    draw_wall(50, 50, 10, 400)     # 1 parede esquerda vertical externa
    draw_wall(50, 50, 350, 10)     # 2 parede topo esquerda externa
    draw_wall(390, 50, 10, 400)    # 3 parede vertical direita interna (parte superior)
    draw_wall(50, 450, 100, 10)    # 4
    draw_wall(110, 150, 10, 200)    # 5 parede esquerda do quadrado interno
    draw_wall(110, 140, 150, 10)   # 6 topo do quadrado interno
    draw_wall(110, 350, 160, 10)   # 7 base do quadrado interno
    
    draw_wall(150, 450, 10, 140)   #8
    draw_wall(50, 590, 110, 10)    # 9 parte que liga o quadrado interno ao lado direito
    draw_wall(50, 590, 10, 150)    #10
    draw_wall(50, 740, 220, 10)   #11
    draw_wall(270, 350, 10, 400)   #12
    draw_wall(260, 140, 10, 160)    # 13 reforço da parede vertical direita superior
    draw_wall(260, 300, 70, 10)   #14
    draw_wall(320, 300, 10, 300)   # 15vertical direita externa

    draw_wall(390, 450, 160, 10)   # 16 base direita
    draw_wall(550, 450, 10, 220)   #17
    draw_wall(320, 600, 160, 10)   #18
    draw_wall(480, 600, 10, 140)   #19
    draw_wall(480, 740, 210, 10)   #20
    draw_wall(550, 670, 50, 10)  #21
    draw_wall(600, 410, 10, 270)  #22
    draw_wall(690, 260, 10, 490)   #23
    draw_wall(460, 410, 150, 10)  #24
    draw_wall(460, 200, 10, 210)  #25
    draw_wall(460, 200, 230, 10)   # 26 topo da parte direita
    draw_wall(690, 50, 10, 160)    # 27 topo direita vertical
    draw_wall(690, 260, 50, 10)  #28
    draw_wall(740, 50, 10, 220)   #29
    draw_wall(690,50, 50, 10)


# Função para verificar colisão com barreiras
def check_collision(new_rect):
    for wall in barreiras:
        if new_rect.colliderect(wall):
            return True
    return False

# Loop principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    new_pos = player_pos[:]
    if keys[pygame.K_LEFT]:
        new_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        new_pos[0] += player_speed
    if keys[pygame.K_UP]:
        new_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        new_pos[1] += player_speed

    draw_maze()

    # Cria um retângulo simulado com a nova posição para checar colisão
    new_player_rect = pygame.Rect(new_pos[0], new_pos[1], player_size, player_size)
    if not check_collision(new_player_rect):
        player_pos = new_pos

    # Desenha o jogador
    pygame.draw.rect(screen, YELLOW, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.flip()
    clock.tick(60)