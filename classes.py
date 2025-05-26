# Arquivo para definir as classes do jogo
import pygame
from os import path
from funções_variáveis import *
# ----- Inicializa assets
peixe_img = pygame.image.load("assets/peixe_sem_fundo.png").convert_alpha()
peixe_img = pygame.transform.scale(peixe_img, (30, 30))
gato_img = pygame.image.load("assets/gato_magro_sem_fundo.png").convert_alpha()
gato_img = pygame.transform.scale(gato_img, (50, 50))

WIDTH = 800
HEIGHT = 800
# Classe do Player

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(50, 50, 50, 50) #coordenadas iniciais do gato, tamanho do gato
        self.speedx = 0
        self.speedy = 0
        self.image = gato_img
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