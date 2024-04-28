import pygame
from pygame.locals import *
from sys import exit
pygame.init()

black = (0,0,0)

largura = 640
altura = 480

tela = pygame.display.set_mode((largura,altura))

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites_test/attack_1.png'))
        self.sprites.append(pygame.image.load('sprites_test/attack_2.png'))
        self.sprites.append(pygame.image.load('sprites_test/attack_3.png'))
        self.sprites.append(pygame.image.load('sprites_test/attack_4.png'))
        self.sprites.append(pygame.image.load('sprites_test/attack_5.png'))
        self.sprites.append(pygame.image.load('sprites_test/attack_6.png'))
        self.sprites.append(pygame.image.load('sprites_test/attack_7.png'))
        self.sprites.append(pygame.image.load('sprites_test/attack_8.png'))
        self.sprites.append(pygame.image.load('sprites_test/attack_9.png'))
        self.sprites.append(pygame.image.load('sprites_test/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(128*5,64*5))# reescala da sprite - transform.scale(imagem,(largura,altura))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100,100
        self.animar = False

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image,(128*5,64*5))
    def atacar(self):
        self.animar = True


todas_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_sprites.add(sapo)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    tela.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()

    todas_sprites.draw(tela)
    todas_sprites.update()

    pygame.display.flip()