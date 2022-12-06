import pygame

WIDTH = 800
HEIGHT = 400

class Platform(pygame.sprite.Sprite):
    #inicializando a classe
    def __init__(self):
        super(Platform, self).__init__()
        #Definindo a parte visual da plataforma
        self.surf = pygame.image.load("assets/pixil-frame-2.png")
        self.surf = pygame.transform.scale(self.surf, (WIDTH, 30))
        #Localização da plataforma
        self.rect = self.surf.get_rect(
            center = (
                (WIDTH/2),
                (HEIGHT- 10),
            )
        )