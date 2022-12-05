import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, heigth):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("assets/pixil-frame-barrel.png")
        self.surf = pygame.transform.scale(self.surf, (150, 150))
        self.rect = self.surf.get_rect(
            center = (
                random.randint(width + 20, width + 100),
                heigth-35
            )
        )
        self.speed = 4

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
