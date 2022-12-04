import pygame
from pygame.locals import *

vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.12
WIDTH = 600
HEIGHT = 450


class Player(pygame.sprite.Sprite) :
    def __init__(self, width, heigth):
        super(Player, self).__init__()
        self.width = width
        self.heigth = heigth
        self.surf = pygame.image.load("assets/pixil-frame-bro.png")
        self.surf = pygame.transform.scale(self.surf, (150, 150))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 385))
        self.vel = vec((0,0))
        self.acc = vec((0,0))

    def move(self, keys_pressed):
        self.acc = vec((0,0.5))
        if keys_pressed[ord("a")]:
            self.acc.x = -ACC
        if keys_pressed[ord("d")]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos