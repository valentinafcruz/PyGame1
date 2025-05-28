import pygame
# Função para checar colisão com barreiras
def check_collision(nova_posicao, barreiras):
    for wall in barreiras:
        if nova_posicao.colliderect(wall):
            return True
    return False

