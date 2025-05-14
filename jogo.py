# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame')


# ----- Inicia assets
fundo_img = pygame.display.set_mode((WIDTH, HEIGHT))
parede = pygame.image.load('assets\maze_pixel_art-removebg-preview.png').convert_alpha()
parede = pygame.transform.scale(parede, (WIDTH, HEIGHT))

# ----- Inicia estruturas de dados
class player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speedx = 0
        self.speedy = 0 
        self.image = pygame.image.load('assets/gato_sem_fundo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
    def move(self):
        self.x += self.speedx
        self.y += self.speedy
    def draw(self):
        window.blit(self.image, (self.x, self.y))
 
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
                    player.speedx = -8
                    player.speedy = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                    player.speedy = 0
                if event.key == pygame.K_UP:        
                    player.speedy =- 8
                    player.speedx = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 8
                    player.speedx = 0
    # ----- Gera saídas
    imagem = pygame.transform.scale(fundo_img, (WIDTH, HEIGHT))
    # ----- desenha fundo
    window.fill((0, 0, 0))
    window.blit(parede, (0, 0)) 
    player.move()  # Move o personagem
    player.draw()
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados