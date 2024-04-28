import pygame
from pygame.locals import *
from sys import exit
import os
pygame.init()
#------------------------------------------------------------------------------------------------------------------
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal,'sprites_test')

largura = 640
altura = 480

tela = pygame.display.set_mode((largura,altura)) #cria a janela 

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens,'dino_spritesheet.png')).convert_alpha() #seleciona a spritesheet
#------------------------------------------------------------------------------------------------------------------
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens = []
        for i in range(3):
            img = sprite_sheet.subsurface((i*32,0),(32,32)) # recorta a spritesheet =  .subsurface((posi_x_init,posi_Y_init),(tamanho_x,tamanho_y))
            img = pygame.transform.scale(img,(32*1,32*1))
            self.imagens.append(img)
            

        self.index_lista = 0
        self.image = self.imagens[self.index_lista]

        self.rect = self.image.get_rect()
        self.rect.center = largura/2,altura/2

    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens[int(self.index_lista)]
        
        
        
todas_sprites = pygame.sprite.Group()
sprite = Sprite()
todas_sprites.add(sprite)

while True : #loop do jogo 
    
    tela.fill((0,0,0))
    for event in pygame.event.get(): #verifica se tem um evento no jogo 
        if event.type == QUIT: # quita do jogo 
            pygame.quit()
            exit()

    todas_sprites.draw(tela)
    todas_sprites.update()

    pygame.display.flip()