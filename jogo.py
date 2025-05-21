# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from init_screen import init_screen
from gameover import game_over_screen 
from inimigo import Inimigo, TiroInimigo      

pygame.init()

# ----- Gera tela principal
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame')


# ----- Inicia assets
fundo_img = pygame.display.set_mode((WIDTH, HEIGHT))
peixe_img = pygame.image.load("assets/peixe_sem_fundo.png").convert_alpha()
peixe_img = pygame.transform.scale(peixe_img, (30, 30))

# Cores
BLACK = (0, 0, 0)
YELLOW = (255,215,0)

# ----- Inicia estruturas de dados
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(50, 50, 50, 50) #coordenadas iniciais do gato, tamanho do gato
        self.speedx = 0
        self.speedy = 0
        self.image = pygame.image.load('assets/gato_magro_sem_fundo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

    def move(self):

        nova_posicao = pygame.Rect(self.rect.x + self.speedx, self.rect.y + self.speedy, self.rect.width, self.rect.height)
        if not check_collision(nova_posicao):
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

# Função para verificar colisão com barreiras
def check_collision(nova_posicao):
    for wall in barreiras:
        if nova_posicao.colliderect(wall):
            return True
    return False

# Classe do peixe
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

    Peixe(60, 410),
    Peixe(200, 410),
    Peixe(300, 410),
  
    # escrever outros peixes...
]
# Lista para armazenar retângulos das paredes (barreiras)
barreiras = []
# ----- Função para desenhar o labirinto 
def draw_maze():
    window.fill(BLACK)

    def draw_wall1(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(window, YELLOW, rect)
        barreiras.append(rect)

    barreiras.clear()
    #Paredes - Labirinto 1
    #cantos
    draw_wall1(0,0,50,800)
    draw_wall1(0,0,800,50)
    draw_wall1(0,750,800,50)
    draw_wall1(750,0,50,800)
    #resto das paredes
    draw_wall1(100,100,50,250)
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
# ===== Loop principal =====

clock = pygame.time.Clock()
FPS = 30
player = player()

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

# Inicia o jogo 
while state != QUIT:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            state = QUIT
        # Verifica se apertou alguma tecla.
        if state == GAME:
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if player.speedx == 0 and player.speedy == 0:
                    if event.key == pygame.K_LEFT:
                        player.speedx = -25
                        player.speedy = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 25
                        player.speedy = 0
                    if event.key == pygame.K_UP:        
                        player.speedy =- 25
                        player.speedx = 0
                    if event.key == pygame.K_DOWN:
                        player.speedy = 25
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
    # Atualiza lista de peixes (remove os comidos)
    peixes = [peixe for peixe in peixes if not peixe.foi_comido(player.rect)]

    for peixe in peixes:
        peixe.desenhar(window)

    # ----- Gera saídas
    player.move()  # Move o personagem
    player.draw() # Desenha o personagem
    pygame.display.update()  # Atualiza a tela
    draw_maze() # Desenha o labirinto
    # Verifica se o jogador colidiu com as barreiras
