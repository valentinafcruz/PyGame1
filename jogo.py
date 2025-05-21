# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from init_screen import init_screen
from gameover2 import game_over_screen     
from inimigo import Inimigo, TiroInimigo      

pygame.init()

# ----- Gera tela principal
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FatCatRush')


# ----- Inicia assets
fundo_img = pygame.display.set_mode((WIDTH, HEIGHT))
parede = pygame.image.load('assets/maze_pixel_art-removebg-preview.png').convert_alpha()
parede = pygame.transform.scale(parede, (WIDTH, HEIGHT))

# Cores
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)

# ----- Inicia estruturas de dados
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/gato_sem_fundo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (47, 50))
        self.rect = self.image.get_rect(topleft=(50, 50))
        self.speedx = 0
        self.speedy = 0

    def move(self):
        new_rect = pygame.Rect(self.rect.x + self.speedx, self.rect.y + self.speedy, self.rect.width, self.rect.height)

        if not check_collision(new_rect):
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
                self.speedx = 0
            elif self.rect.left < 0:
                self.rect.left = 0
                self.speedx = 0
            elif self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
                self.speedy = 0
            elif self.rect.top < 0:
                self.rect.top = 0
                self.speedy = 0
            else:
                self.rect.x += self.speedx
                self.rect.y += self.speedy
        else:
            self.speedx = 0
            self.speedy = 0

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# ----- Função para verificar colisão com paredes
def check_collision(new_rect):
    for wall in barreiras:
        if nova_posicao.colliderect(wall):
            return True
    return False


# ----- Lista para armazenar retângulos das paredes
barreiras = []

# ----- Função para desenhar o labirinto
def draw_maze():
    window.fill(BLACK)

    def draw_wall1(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(window, YELLOW, rect)
        barreiras.append(rect)

    barreiras.clear()

    # Paredes - Labirinto
    draw_wall1(0, 0, 50, 800)
    draw_wall1(0, 0, 800, 50)
    draw_wall1(0, 750, 800, 50)
    draw_wall1(750, 0, 50, 800)

    draw_wall1(100, 100, 50, 250)
    draw_wall1(50, 450, 100, 150)
    draw_wall1(100, 100, 150, 250)
    draw_wall1(250, 300, 50, 500)
    draw_wall1(300, 600, 200, 150)
    draw_wall1(400, 0, 300, 200)
    draw_wall1(400, 200, 50, 250)
    draw_wall1(400, 400, 200, 50)
    draw_wall1(550, 400, 50, 300)
    draw_wall1(700, 250, 50, 550)
    draw_wall1(350, 150, 50, 50)
    draw_wall1(650, 700, 50, 50)

    # def draw_wall2(x, y, w, h):
    #     rect = pygame.Rect(x, y, w, h)
    #     pygame.draw.rect(window, BLACK, rect)
    #     barreiras.append(rect)

    draw_wall2(0, 0, 40, 780)
    draw_wall2(0, 0, 780, 40)
    draw_wall2(0, 760, 780, 40)
    draw_wall2(760, 0, 40, 780)

    draw_wall2(110, 110, 30, 230)
    draw_wall2(60, 460, 80, 130)
    draw_wall2(110, 110, 130, 230)
    draw_wall2(260, 310, 30, 480)
    draw_wall2(310, 610, 180, 130)
    draw_wall2(410, 10, 280, 180)
    draw_wall2(410, 210, 30, 230)
    draw_wall2(410, 410, 180, 30)
    draw_wall2(560, 410, 30, 280)
    draw_wall2(710, 260, 30, 530)
    draw_wall2(360, 160, 30, 30)
    draw_wall2(660, 710, 30, 30)


# ===== Loop principal =====

clock = pygame.time.Clock()
FPS = 30

player = Player()

INIT = 0
GAME = 1
QUIT = 2
GAMEOVER = 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
state = init_screen(screen, WIDTH, HEIGHT)

# ----- Grupos de sprites
grupo_inimigos = pygame.sprite.Group()
grupo_tiros_inimigos = pygame.sprite.Group()

# ----- Cria inimigos
inimigo1 = Inimigo(300, 90, 'baixo')
inimigo2 = Inimigo(600, 220, 'direita')
inimigo3 = Inimigo(235, 370, 'esquerda')
grupo_inimigos.add(inimigo1, inimigo2, inimigo3)


# ===== Loop =====
while state != QUIT:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = QUIT

        if state == GAME:
            if event.type == pygame.KEYDOWN:
                if player.speedx == 0 and player.speedy == 0:
                    if event.key == pygame.K_LEFT:
                        player.speedx = -15
                        player.speedy = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 15
                        player.speedy = 0
                    if event.key == pygame.K_UP:
                        player.speedy = -15
                        player.speedx = 0
                    if event.key == pygame.K_DOWN:
                        player.speedy = 15
                        player.speedx = 0

    if state == GAMEOVER:
        game_over_screen(screen, WIDTH, HEIGHT)
            

    if state == GAME:
        # ----- Atualizações
        grupo_inimigos.update(grupo_tiros_inimigos)
        grupo_tiros_inimigos.update(barreiras)

        # Verifica colisão dos tiros com o player
        if pygame.sprite.spritecollide(player, grupo_tiros_inimigos, True):
            state = GAMEOVER
        if pygame.sprite.spritecollide(player, grupo_inimigos, False):
            state = GAMEOVER

        # ----- Desenho
        draw_maze()
        player.move()
        player.draw()

        grupo_inimigos.draw(screen)
        grupo_tiros_inimigos.draw(screen)

        pygame.display.update()

# ===== Finalização =====
pygame.quit()
