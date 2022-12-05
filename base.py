# Importa o módulo do pygame
import pygame
from pygame.locals import*
import kong
import barrel
import cloud
import plataforma

pygame.mixer.init()

# inicializa o pygame
pygame.init()
pygame.display.set_caption("Jogo Donkey Kong")

# https://instrumentalfx.co/steven-universe-soundtrack-opening-instrumental/
# pygame.mixer.music.load("assets/steven-universe-instrumental.mp3")
# pygame.mixer.music.play(loops=-1)

# constante para largura e altura da tela
width = 800
height = 400
puloMax = 150

player = kong.Player(width, height)
barril = barrel.Enemy(width, height)
barril = pygame.sprite.Group()
nuvem = cloud.Cloud(width, height)
nuvem = pygame.sprite.Group()
chao = plataforma.Platform()

all_sprite = pygame.sprite.Group()
all_sprite.add(chao)
all_sprite.add(player)

window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1700)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.jump()
            elif player.vel.y == -15:
                player.vel.y = 15
    
        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = barrel.Enemy(width, height)
            barril.add(new_enemy)
            all_sprite.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = cloud.Cloud(width, height)
            nuvem.add(new_cloud)
            all_sprite.add(new_cloud) 
    
    pressed_keys = pygame.key.get_pressed()

    player.move(pressed_keys)
    barril.update()
    nuvem.update()
    
    window.fill((135, 206, 235))

    for entity in all_sprite:
        window.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollide(player, barril, dokill = True):
        player.kill()
        running = False
        
    pygame.display.flip()

    clock.tick(30)

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()

# https://coderslegacy.com/python/pygame-gravity-and-jumping/
