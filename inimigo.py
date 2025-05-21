import pygame

# === Classes ===

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


class TiroInimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao):
        super().__init__()
        self.image = pygame.image.load('assets/Osso Tiro.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade = 13
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




        




