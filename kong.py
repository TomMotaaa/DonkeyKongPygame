import pygame
from pygame.locals import *
import plataforma

vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.12
WIDTH = 800
HEIGHT = 400
chao = plataforma.Platform()


class Player(pygame.sprite.Sprite) :
    def __init__(self, width, heigth):
        super(Player, self).__init__()
        self.width = width
        self.heigth = heigth
        self.surf = pygame.image.load("assets/pixil-frame-1.png")
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 78))

        self.pos = vec((10, 385))
        self.vel = vec((0,0))
        self.acc = vec((0,0))

    def limite(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.acc.x = ACC
        if self.rect.right > self.width:
            self.rect.right = self.width
            self.acc.x = -ACC
        if self.rect.bottom >= self.heigth-23:
            self.rect.bottom = self.heigth
            self.vel.y = -3

    def move(self, keys_pressed):
        self.acc = vec((0,0.5))
        if keys_pressed[ord("a")]:
            self.acc.x = -ACC
        if keys_pressed[ord("d")]:
            self.acc.x = ACC
        self.limite()

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def update(self):
        player = Player(WIDTH, HEIGHT)
        hits = pygame.sprite.spritecollide(player, platforms, False)  
        if player.vel.y > 0:   
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -10


platforms = pygame.sprite.Group()
platforms.add(chao)