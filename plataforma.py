import pygame
WIDTH = 600
HEIGHT = 450

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.surf = pygame.image.load("assets/pixil-frame-earth.png")
        self.surf = pygame.transform.scale(self.surf, (WIDTH, 350))
        self.rect = self.surf.get_rect(
            center = (
                (WIDTH/2),
                (HEIGHT- 10),
            )
        )