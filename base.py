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
#pygame.mixer.music.load("assets/steven-universe-instrumental.mp3")
#pygame.mixer.music.play(loops=-1)

# constante para largura e altura da tela
width = 800
height = 400

#Scor
gameOver = False
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 25)    
textX = 10
textY = 10
gameX = 350
gameY = 200

#Inicializando as classes
player = kong.Player(width, height)
barril = barrel.Enemy(width, height)
barril = pygame.sprite.Group()
nuvem = cloud.Cloud(width, height)
nuvem = pygame.sprite.Group()
chao = plataforma.Platform()

#Renderizando o Jogador e a Chão
all_sprite = pygame.sprite.Group()
all_sprite.add(chao)
all_sprite.add(player)

#Tela do jogo
window = pygame.display.set_mode((width, height))

#Função do scor
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    window.blit(score, (x,y))
    
def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [width/10, height/2])

#Inicializa o "Clock"
clock = pygame.time.Clock()

#Evento de spawn utilizando delay
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1700)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

#Rodar o Jogo
running = True
while running:
    while gameOver:
        
        texto("Fim de Jogo, para continuar tecle B, ou N para sair", (255,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            #Evento para fechar o jogo
            if event.type == QUIT:
                running = False
                gameOver = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    running = True
                    gameOver = False
                    all_sprite.add(player)
                    score_value = 0
                if event.key == pygame.K_n:
                    running = False
                    gameOver = False
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
               player.isJump = True
        #Evento para fechar o jogo
        if event.type == QUIT:
            running = False
            
        #Evento para criar os inimigos no jogo
        elif event.type == ADDENEMY:
            new_enemy = barrel.Enemy(width, height)
            barril.add(new_enemy)
            all_sprite.add(new_enemy)
            #Contagem do scor a cada inimigo spwnado
            score_value +=  1
            
        #Evento para spawnar as nuvens
        elif event.type == ADDCLOUD:
            new_cloud = cloud.Cloud(width, height)
            nuvem.add(new_cloud)
            all_sprite.add(new_cloud) 
    
    #Faz um get das chaves que são ser pressionadas
    pressed_keys = pygame.key.get_pressed()

    #Atualiza o jogador
    player.update()
    #Movimentação do jogador1222
    player.move(pressed_keys)
    
    #Atualiza o inimigo
    barril.update()
    #Atualiza a nuvem
    nuvem.update()
    
    #Cor do fundo da tela
    window.fill((135, 206, 235)) 

    #Desenha os sprites na tela
    for entity in all_sprite:
        window.blit(entity.surf, entity.rect)

    #Colisão do barril com o player
    if pygame.sprite.spritecollide(player, barril, dokill = True):
        player.kill()
        gameOver = True
    #Posicão do scor
    show_score(textX, textY )
    player.jump()

    #Vira tudo para o visor
    pygame.display.flip()

    #Fps
    clock.tick(60)

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()

# https://coderslegacy.com/python/pygame-gravity-and-jumping/
