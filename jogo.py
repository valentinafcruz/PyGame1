# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame')


# ----- Inicia assets
fundo_img = pygame.display.set_mode((WIDTH, HEIGHT))
parede = pygame.image.load('assets\maze_pixel_art-removebg-preview.png').convert_alpha()
parede = pygame.transform.scale(parede, (WIDTH, HEIGHT))

# Cores
BLACK = (0, 0, 0)
YELLOW = (255,215,0)

# ----- Inicia estruturas de dados
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(50, 50, 45, 45)
        self.speedx = 0
        self.speedy = 0
        self.image = pygame.image.load('assets/gato_sem_fundo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (47, 50))
    
    def move(self):

        new_rect = pygame.Rect(self.rect.x + self.speedx, self.rect.y + self.speedy, self.rect.width, self.rect.height)
        #pygame.draw.rect(window, (255, 0, 0), new_rect)  # Desenha o retângulo temporário para depuração

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

# Função para verificar colisão com barreiras
def check_collision(new_rect):
    for wall in barreiras:
        if new_rect.colliderect(wall):
            return True
    return False

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

    def draw_wall2(x, y, w, h):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(window, BLACK, rect)
        barreiras.append(rect)

    #moldura
    draw_wall2(0, 0, 40, 780)
    draw_wall2(0, 0, 780, 40)
    draw_wall2(0, 760, 780, 40)
    draw_wall2(760, 0, 40, 780)

    # resto das paredes
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
game = True
clock = pygame.time.Clock()
FPS = 30
player = player()

while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if player.speedx == 0 and player.speedy == 0:
                if event.key == pygame.K_LEFT:
                    player.speedx = -10
                    player.speedy = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 10
                    player.speedy = 0
                if event.key == pygame.K_UP:        
                    player.speedy =- 10
                    player.speedx = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 10
                    player.speedx = 0
    # ----- Gera saídas
    player.move()  # Move o personagem
    player.draw() # Desenha o personagem
    pygame.display.update()  # Atualiza a tela
    draw_maze()   # Desenha o labirinto

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados