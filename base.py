# Import the pygame module
import pygame, time, random

from pygame.locals import *

def main():
    # variáveis do jogo
    quit = False
    x = 0
    y = 0
    # inicia o looping do jogo
    while not quit:
        # muda a cor da tela para azul
        window.fill((135, 206, 235)) 
        # eventos
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
            if event.type == KEYDOWN:
                if event.key == ord("a"):
                    x = x - 50
                if event.key == ord("d"):
                    x = x + 50
                if event.key == ord("w"):
                    y = y - 50
                if event.key == ord("s"):
                    y = y + 50
            
        player = Rect(x, y, 50, 50)
        pygame.draw.rect(window, (204, 0, 255), player)

        # atualiza a tela
        pygame.display.update()
        clock.tick(25)

def main2():
    # variáveis do jogo
    player_stand = pygame.image.load("assets/pixil-frame-bro.png").convert_alpha()
    player_stand = pygame.transform.scale(player_stand, (150, 150))
    quit = False
    x = 0
    y = 0
    while not quit:
        # muda a cor da tela para azul
        window.fill((135, 206, 235)) 
        # eventos
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                quit = True
            
        if keyspressed[ord("a")]:
            x = x - 50
        if keyspressed[ord("d")]:
            x = x + 50
        if keyspressed[ord("w")]:
            y = y - 50
        if keyspressed[ord("s")]:
            y = y + 50
        if  y < 0:
            y = 0
        if y >= window.get_height():
            y = window.get_height()-50
        if x < 0:
            x = 0
        if x >= window.get_width():
            x = window.get_width()-50

        #player = Rect(x, y, 50, 50)
        #pygame.draw.rect(window, (204, 0, 255), player)
        window.blit(player_stand, (x, y))

        # atualiza a tela
        pygame.display.update()
        clock.tick(25)


# Inicializa e roda o jogo
if __name__ == "__main__":
    width, height = 1000, 200
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Jogo Donkey Kong")
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    main2()
    pygame.quit()

