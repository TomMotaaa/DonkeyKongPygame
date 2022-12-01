import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, width, height):
        super(Player, self).__init__()
        self.width = 1000
        self. height = 200
        self.surf = pg.image.load("assets/pixil-frame-bro.png").convert_alpha()
        self.surf = pg.transform.scale(self.surf, (150, 150))
    
    def update(self, pressed_keys):
        if pressed_keys[ord("a")]:
            self.rect.move_ip(-5,0)
        if pressed_keys[ord("w")]:
            self.rect.move_ip(0,-5)
        if pressed_keys[ord("s")]:
            self.rect.move_ip(0,5)
        if pressed_keys[ord("s")]:
            self.rect.move_ip(5,0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.heigth:
            self.rect.bottom = self.heigth      



