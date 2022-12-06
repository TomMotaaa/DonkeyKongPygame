import pygame
import random

#Classe dos inimigo(Barris)
class Enemy(pygame.sprite.Sprite):
    #Inicializando a classe
    def __init__(self, width, heigth):
        super(Enemy, self).__init__()
        #Ajustando tamanho do inimigo visualmente
        self.surf = pygame.image.load("assets/pixil-frame-0.png")
        self.surf = pygame.transform.scale(self.surf, (40, 40))
        #Spawn do inimigo
        self.rect = self.surf.get_rect(
            center = (
                random.randint(width + 20, width + 100),
                heigth-44
            )
        )
        #Velocidade do inimigo
        self.speed = 4

    #Tempo de vida do inimigo
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
