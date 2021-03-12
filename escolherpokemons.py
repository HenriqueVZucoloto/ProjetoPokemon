import pygame
pygame.init()
janela = pygame.display.set_mode((800,600)) #inicializa a janela do jogo
def escolher(): #cena para escolher o pokèmon
    color = (128, 128, 128)#definindo a cor
    janela.fill(color)#pintando o fundo
    pygame.draw.line(janela, (0,0,0), (200,50), (200,550), 5) #linhas do retangulo
    pygame.draw.line(janela, (0,0,0), (600,50), (600,550), 5)
    pygame.draw.line(janela, (0,0,0), (200,50), (600,50), 5)
    pygame.draw.line(janela, (0,0,0), (200,550), (600,550), 5)
    #definindo a fonte
    pygame.font.init()
    fonte = pygame.font.Font('joystix monospace.ttf', 35)
    fonte1 = pygame.font.Font('joystix monospace.ttf', 30)
    #definindo textos
    texto = fonte1.render('ESCOLHA SEU POKÉMON', True, (0,0,0))
    pokemon1 = fonte1.render('PIKACHU', True, (255,255,0))
    pokemon2 = fonte1.render('CHARMANDER', True, (210,105,30))
    pokemon3 = fonte1.render('BULBASAUR', True, (0,128,0))
    pokemon4 = fonte1.render('SQUIRTLE', True, (127,255,212))
    pokemon5 = fonte1.render('MEWTWO', True, (255,0,255))
    #inserindo textos
    janela.blit(texto, (160,5))
    janela.blit(pokemon1, (300,150))
    janela.blit(pokemon2, (300,200))
    janela.blit(pokemon3, (300,250))
    janela.blit(pokemon4, (300,300))
    janela.blit(pokemon5, (300,350))
escolher()
cursor = pygame.image.load('cursor.png')
def posicaoCursor(cursorX, cursorY):
    janela.blit(cursor, (cursorX, cursorY))

cursorX = 270
cursorY = 150


#Loop do jogo
jogando = True
while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

        #Ve se alguma tecla foi pressionada
        if event.type == pygame.KEYDOWN:
            #Se seta para baixo, move o cursor para baixo
            if event.key == pygame.K_DOWN:
                escolher()
                cursorY += 50
                #Não deixa o cursor passar dos limites
                if cursorY > 350:
                    cursorY = 350
            #Se seta para cima, move o cursor para cima
            if event.key == pygame.K_UP:
                escolher()
                cursorY -= 50
                #Não deixa o cursor passar dos limites
                if cursorY < 150:
                    cursorY = 150

    posicaoCursor(cursorX, cursorY)
    pygame.display.update()