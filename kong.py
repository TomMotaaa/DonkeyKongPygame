import pygame
from pygame.locals import *
import plataforma

#Inicializando as variáveis
vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.12
WIDTH = 800
HEIGHT = 400
chao = plataforma.Platform()


class Player(pygame.sprite.Sprite) :
    #Inicializando a classe
    def __init__(self, width, heigth):
        #Definindo o tamanho do jogador
        super(Player, self).__init__()
        self.width = width
        self.heigth = heigth
        self.isJump = False
        self.jumpCount = 10
        self.surf = pygame.image.load("assets/pixil-frame-1.png")
        self.surf = pygame.transform.scale(self.surf, (40, 40))
        #Spawn do player
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 85))

        #Definindo a posição, velocidade e aceleração
        self.pos = vec((10, 385))
        self.vel = vec((0,0))
        self.acc = vec((0,0))

    #Função pra não deixar o personagem sair dos limites da tela
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

    #Função para fazer o movimento do player
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

    #Função de pulo
    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = 0
                self.vel.y -= self.jumpCount*2.2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10


platforms = pygame.sprite.Group()
platforms.add(chao)