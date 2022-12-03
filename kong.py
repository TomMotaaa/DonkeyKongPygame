import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

class Player(pygame.sprite.Sprite) :
    def __init__(self, width, heigth):
        super(Player, self).__init__()
        self.width = width
        self.heigth = heigth
        self.surf = pygame.image.load("assets/pixil-frame-bro.png")
        self.surf = pygame.transform.scale(self.surf, (150, 150))
        self.rect = self.surf.get_rect()

    def update(self, keys_pressed):
        if keys_pressed[ord("w")]:
            self.rect.move_ip(0, -5)
        if keys_pressed[ord("s")]:
            self.rect.move_ip(0, 5)
        if keys_pressed[ord("a")]:
            self.rect.move_ip(-5, 0)
        if keys_pressed[ord("d")]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.heigth:
            self.rect.bottom = self.heigth 