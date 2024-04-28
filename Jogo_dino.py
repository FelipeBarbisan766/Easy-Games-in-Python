from typing import Any
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange
pygame.init()
#------------------------------------------------------------------------------------------------------------------
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal,'sprites_test')

#------------------------------------------------------------------------------------------------------------------
branco = (255,255,255)

largura = 640
altura = 480

tamanho_chao = 2 * 32
velocidade_chao = 10

tamanho_dino = 3
velocidade_dino = 0.25
posicao_dinoX = 100
posicao_dinoY = altura-tamanho_chao

tamanho_nuvem = 3
velocidade_nuvem = 10

#------------------------------------------------------------------------------------------------------------------
tela = pygame.display.set_mode((largura,altura)) #cria a janela 
pygame.display.set_caption("Dino Game") #titulo da tela
clock = pygame.time.Clock()#inicia o clock
#------------------------------------------------------------------------------------------------------------------
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens,'dino_spritesheet.png')).convert_alpha()
#------------------------------------------------------------------------------------------------------------------
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dino = []
        for i in range(3):
            img = sprite_sheet.subsurface((i*32,0),(32,32)) # recorta a spritesheet =  .subsurface((posi_x_init,posi_Y_init),(tamanho_x,tamanho_y))
            img = pygame.transform.scale(img,(32*tamanho_dino,32*tamanho_dino))
            self.imagens_dino.append(img)
            

        self.index_lista = 0
        self.image = self.imagens_dino[self.index_lista]

        self.rect = self.image.get_rect()
        self.rect.center = (posicao_dinoX,posicao_dinoY)

    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += velocidade_dino
        self.image = self.imagens_dino[int(self.index_lista)]
        self.rect.center = (posicao_dinoX,posicao_dinoY)
#------------------------------------------------------------------------------------------------------------------
class Nuvem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32*7,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*tamanho_nuvem,32*tamanho_nuvem))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50,200,50)# randomizador com intervalo = randrange(val_init,val_fin,intervalo)
        self.rect.x = largura - randrange(30,300,90)
        
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.y = randrange(50,200,50)
            self.rect.x = largura + randrange(30,300,90)
        self.rect.x -= velocidade_nuvem
#------------------------------------------------------------------------------------------------------------------
class Chao(pygame.sprite.Sprite):
    def __init__(self,pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32*6,0),(32,32))
        self.image = pygame.transform.scale(self.image,(tamanho_chao,tamanho_chao))
        self.rect = self.image.get_rect()
        self.rect.y = altura - tamanho_chao
        self.rect.x = pos_x * tamanho_chao

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= velocidade_chao
#------------------------------------------------------------------------------------------------------------------
todas_sprites = pygame.sprite.Group()
dino = Dino()
todas_sprites.add(dino)
for i in range(largura*2//tamanho_chao):
    chao = Chao(i)
    todas_sprites.add(chao)
for i in range (4):
    nuvem = Nuvem()
    todas_sprites.add(nuvem)
#------------------------------------------------------------------------------------------------------------------
while True : #loop do jogo 
    clock.tick(30) #frame 
    tela.fill(branco)
    for event in pygame.event.get(): #verifica se tem um evento no jogo 
        if event.type == QUIT: # quita do jogo 
            pygame.quit()
            exit()
        
                
    if pygame.key.get_pressed()[K_a]:
        posicao_dinoX -= 20  
    if pygame.key.get_pressed()[K_d]:
        posicao_dinoX += 20   
    if pygame.key.get_pressed()[K_SPACE]:
        posicao_dinoY -= 10
        if posicao_dinoY == altura/2:
            pass
       
            
    if posicao_dinoY < altura-tamanho_chao:
        posicao_dinoY += 10
    todas_sprites.draw(tela)
    todas_sprites.update()

    pygame.display.flip()