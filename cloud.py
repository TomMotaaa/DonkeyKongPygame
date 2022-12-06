import pygame
import random

class Cloud(pygame.sprite.Sprite):
    #Inicializando a classe
    def __init__(self, width, heigth):
        super(Cloud, self).__init__()
        #Ajustando o tamanho da nuvem visualmente
        self.surf = pygame.image.load("assets/pixil-frame-cloud.png")
        self.surf = pygame.transform.scale(self.surf, (150, 150))
        #Spawn da nuvem
        self.rect = self.surf.get_rect(
            center=(
                random.randint(width + 20, width + 100),
                random.randint(0, heigth-80),
            )
        )

    #Tempo de vida da nuvem
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()