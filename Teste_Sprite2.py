import pygame
from pygame.locals import *
from sys import exit
pygame.init()

black = (0,0,0)

largura = 640
altura = 480

tamanho_slime = [32*4,32*4]

tela = pygame.display.set_mode((largura,altura))

class Slime(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites_test/slime_0.png'))
        self.sprites.append(pygame.image.load('sprites_test/slime_1.png'))
        self.sprites.append(pygame.image.load('sprites_test/slime_2.png'))
        self.sprites.append(pygame.image.load('sprites_test/slime_3.png'))
        self.sprites.append(pygame.image.load('sprites_test/slime_4.png'))
        self.sprites.append(pygame.image.load('sprites_test/slime_5.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,tamanho_slime)# reescala da sprite - transform.scale(imagem,(largura,altura))

        self.rect = self.image.get_rect()
        self.rect.center = largura/2,280
        

    def update(self):
        
        self.atual = self.atual + 0.4
        if self.atual >= len(self.sprites):
            self.atual = 0
            self.animar = False
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image,tamanho_slime)
    


todas_sprites = pygame.sprite.Group()
slime = Slime()
todas_sprites.add(slime)

imagen_fundo = pygame.image.load('sprites_test/background.jpg').convert()
imagen_fundo = pygame.transform.scale(imagen_fundo,(largura,altura))

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    tela.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    tela.blit(imagen_fundo,(0,0))        

    todas_sprites.draw(tela)
    todas_sprites.update()

    pygame.display.flip()