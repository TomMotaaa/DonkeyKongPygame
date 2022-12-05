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
                random.randint(0, heigth-80)
            )
        )
        self.speed = random.randint(3, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
