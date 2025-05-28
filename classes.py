# Arquivo para definir as classes do jogo
# Importando bibliotecas necessárias
import pygame
from os import path
from mapas_das_fases import *

pygame.init()
# ----- Inicializa assets do peixe
peixe_img = pygame.image.load("assets/peixe_sem_fundo.png").convert_alpha()
peixe_img = pygame.transform.scale(peixe_img, (30, 30))
# ----- Inicializa assets do gato
gato_imgs = [
    pygame.image.load("assets/gato_magro_sem_fundo.png"),
    pygame.image.load("assets/gato_medio_sem_fundo.png"),
    pygame.image.load("assets/gato_gordo_sem_fundo.png")
]

# Redimensiona as imagens
gato_imgs = [pygame.transform.scale(img, (50, 50)) for img in gato_imgs]

WIDTH = 800
HEIGHT = 800

# ----- Classe do player (gato)

class player(pygame.sprite.Sprite):
    def __init__(self, imagens):
        super().__init__()
        self.imagens = imagens
        self.nivel = 0 # Nível inicial do gato
        self.image = self.imagens[self.nivel]
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0

    def move(self, barreiras):
        nova_posicao = pygame.Rect(self.rect.x + self.speedx, self.rect.y + self.speedy, self.rect.width, self.rect.height)
        if not check_collision(nova_posicao, barreiras):
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

    def draw(self, screen):
        self.image = self.imagens[self.nivel]
        screen.blit(self.image, self.rect.topleft)
    
    def evoluir(self):
        if self.nivel < len(self.imagens) - 1:
            self.nivel += 1

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

# Classe do inimigo
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao):
        super().__init__()
        self.image = pygame.image.load('assets/Cachorro Inimigo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (47, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.direcao = direcao
        self.tempo_ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = 1000  # Intervalo de tiro (ms)

    def update(self, grupo_tiros):
        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_tiro > self.intervalo_tiro:
            
            if self.direcao == 'cima':
                x = self.rect.centerx
                y = self.rect.top
            elif self.direcao == 'baixo':
                x = self.rect.centerx
                y = self.rect.bottom
            elif self.direcao == 'esquerda':
                x = self.rect.left
                y = self.rect.centery
            elif self.direcao == 'direita':
                x = self.rect.right
                y = self.rect.centery

            tiro = TiroInimigo(x, y, self.direcao)
            grupo_tiros.add(tiro)
            self.tempo_ultimo_tiro = agora

# Classe do tiro do inimigo
class TiroInimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao):
        super().__init__()
        self.image = pygame.image.load('assets/Osso Tiro.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade = 2  # Velocidade do tiro
        self.direcao = direcao # Direção inicial

    def update(self, paredes):
        if self.direcao == 'cima':
            self.rect.y -= self.velocidade
        elif self.direcao == 'baixo':
            self.rect.y += self.velocidade
        elif self.direcao == 'esquerda':
            self.rect.x -= self.velocidade
        elif self.direcao == 'direita':
            self.rect.x += self.velocidade

        for parede in paredes:
            if self.rect.colliderect(parede):
                self.kill()
                break