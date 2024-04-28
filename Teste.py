import pygame 
from pygame.locals import * #inporta todos os codigos
from sys import exit #inporta o btn exit
from random import randint

pygame.init() #inicia o pygame

font = pygame.font.SysFont('arial',40,False,False)#configura a fonte de texto - variavel = pygame.font.SysFont(tipo,tamanho,bold,italico)

altura = 480
largura = 640
x = largura/2 - 40
y = altura/2 - 40

pontos = 0

x_azul = randint(20,600)#randomizador de posição randint(num_inicial,num_final)
y_azul = randint(20,400)

tela = pygame.display.set_mode((largura,altura)) #cria a janela 
pygame.display.set_caption("Teste") #titulo da tela
clock = pygame.time.Clock()#inicia o clock

while True : #loop do jogo 
    clock.tick(60) #frame 
    tela.fill((0,0,0))#preechimento da tela 
    mensagem = f'Pontos:{pontos}'#texto que irá aparecer na tela 
    text_formatado = font.render(mensagem,True,(255,255,255)) # formatação/compilação do texto - variavel=fonte.render(texto,quadriculado,cor)
    for event in pygame.event.get() : #verifica se tem um evento no jogo 
        if event.type == QUIT: # quita do jogo 
            pygame.quit()
            exit()
        
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         x = x - 20
        #     if event.key == K_d:
        #         x = x + 20
        #     if event.key == K_w:
        #         y = y - 20
        #     if event.key == K_s:
        #         y = y + 20    

    if pygame.key.get_pressed()[K_a]:
        x = x - 20  
    if pygame.key.get_pressed()[K_d]:
        x = x + 20   
    if pygame.key.get_pressed()[K_w]:
        y = y - 20   
    if pygame.key.get_pressed()[K_s]:
        y = y + 20        

    ret_red = pygame.draw.rect(tela,(255,0,0),(x,y,80,80)) #cria um quadrado - rect(local,(R,G,B),(posição x,posição y,largura,altura))
    ret_blue = pygame.draw.rect(tela,(0,0,255),(x_azul,y_azul,80,80))
    # pygame.draw.circle(tela,(0,0,255),(400,80),40) #cria um Circulo - circle(local,(R,G,B),(posição x,posição y),raio)
    # pygame.draw.line(tela,(0,255,0),(300,0),(300,480),5) #cria uma Linha - line(local,(R,G,B),(posição inicial x,posição inicial y),(posição final x,posição final y), espessura)
    
    if ret_red.colliderect(ret_blue):
        x_azul = randint(20,600)#randomizador de posição randint(num_inicial,num_final)
        y_azul = randint(20,400)
        pontos = pontos + 1

    # if y >= altura:
    #     y = 0
    # y = y + 1

    tela.blit(text_formatado,(450,40)) #Cria na tela o retangulo com o texto - local.blit(texto,cor)

    pygame.display.update() # atualiza a tela 
        