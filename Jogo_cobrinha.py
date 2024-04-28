import pygame 
from pygame.locals import * #inporta todos os codigos
from sys import exit #inporta o btn exit
from random import randint

pygame.init() #inicia o pygame

font = pygame.font.SysFont('arial',40,False,False)#configura a fonte de texto - variavel = pygame.font.SysFont(tipo,tamanho,bold,italico)

altura = 480
largura = 640

x_cobra = largura/2
y_cobra = altura/2

x_maca = randint(20,600)#randomizador de posição randint(num_inicial,num_final)
y_maca = randint(20,400)

velocidade = 10
x_controle = velocidade
y_controle = 0

pontos = 0
lista_cobra = []
comprimento = 4
morreu = False

tela = pygame.display.set_mode((largura,altura)) #cria a janela 
pygame.display.set_caption("Game Snake") #titulo da tela
clock = pygame.time.Clock()#inicia o clock

def reiniciar_jogo():
    global pontos,comprimento,x_cobra,x_controle,y_cobra,y_controle,lista_cobra,lista_cabeca,x_maca,y_maca,morreu
    pontos = 0
    comprimento = 4
    x_cobra = largura/2
    y_cobra = altura/2 
    lista_cabeca = []
    lista_cobra = [] 
    x_maca = randint(20,600)        
    y_maca = randint(20,400)    
    morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x,y]
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],20,20))

while True : #loop do jogo 
    clock.tick(20) #frame 
    tela.fill((255,255,255))#preechimento da tela 
    mensagem = f'Pontos:{pontos}'#texto que irá aparecer na tela 
    text_formatado = font.render(mensagem,True,(0,0,0)) # formatação/compilação do texto - variavel=fonte.render(texto,quadriculado,cor)
    
    for event in pygame.event.get(): #verifica se tem um evento no jogo 
        if event.type == QUIT: # quita do jogo 
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d or event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w or event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s or event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade        

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20)) #cria um quadrado - rect(local,(R,G,B),(posição x,posição y,largura,altura))
    maca = pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,20,20))

    if cobra.colliderect(maca):
        x_maca = randint(20,600)#randomizador de posição randint(num_inicial,num_final)
        y_maca = randint(20,400)
        pontos = pontos + 1
        comprimento = comprimento + 2

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True
        font2 = pygame.font.SysFont('arial',15,True,False)
        mensagem_final = "Game Over Precione space para continuar"
        text_final = font2.render(mensagem_final,True,(255,255,255))
        ret_text = text_final.get_rect()
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        reiniciar_jogo()
            ret_text.center = (largura//2,altura//2)
            tela.blit(text_final,ret_text)
            pygame.display.update()    

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    

    tela.blit(text_formatado,(450,40)) #Cria na tela o retangulo com o texto - local.blit(texto,cor)

    pygame.display.update() # atualiza a tela 
        