import pygame
pygame.init()

#Cria a janela
janela = pygame.display.set_mode((800,600)) #inicializa a janela do jogo

#Muda o nome
pygame.display.set_caption('HOJE TEM GOL DO RIBAMAR')

class Cenas:
    #Carrega as imagens
    def __init__(self):
        self.fundoBatalha = pygame.image.load('FundoPokemon.png')
        self.caixaTexto = pygame.image.load('text_bar.png')
        self.opcoesBatalha = pygame.image.load('fgt_options.png')
        self.barra1 = pygame.image.load('barra_1.png')
        self.barra2 = pygame.image.load('barra_2.png')
        self.caixaGolpes = pygame.image.load('pp_bar.png')
    
    #Cria o cenário da batalha
    def cenarioInicialBatalha(self):
        #Ajusta o tamanho das imagens
        self.fundoBatalha = pygame.transform.scale(self.fundoBatalha, (800,440))
        self.caixaTexto = pygame.transform.scale(self.caixaTexto, (800,160))
        self.opcoesBatalha = pygame.transform.scale(self.opcoesBatalha, (400, 160))
        self.barra1 = pygame.transform.scale(self.barra1, (330,100))
        self.barra2 = pygame.transform.scale(self.barra2, (375,126))

        #Mostra as imagens na tela
        janela.blit(self.fundoBatalha, (0,0))
        janela.blit(self.caixaTexto, (0,440))
        janela.blit(self.opcoesBatalha, (400,440))
        janela.blit(self.barra1, (30,30))
        janela.blit(self.barra2, (415,310))

    #Abre a pagina de golpes
    def paginaGolpes(self):
        self.caixaGolpes = pygame.transform.scale(self.caixaGolpes, (800,160))
        janela.blit(self.caixaGolpes, (0,440))
    
    #Abre a pagina da batalha
    def paginaBatalha(self):
        janela.blit(self.caixaTexto, (0,440))
        janela.blit(self.opcoesBatalha, (400,440))

#Carrega e printa o cursor        
cursor = pygame.image.load('cursor.png')
def posicaoCursor(cursorX, cursorY):
    janela.blit(cursor, (cursorX, cursorY))
#Posição inicial do cursor
cursorX, cursorY = 425, 480

cenas = Cenas()
cenas.cenarioInicialBatalha()

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
                cenas.paginaBatalha()
                cursorY += 53
                #Não deixa o cursor passar dos limites
                if cursorY > 550:
                    cursorY = 533
            #Se seta para cima, move o cursor para cima
            elif event.key == pygame.K_UP:
                cenas.paginaBatalha()
                cursorY -= 53
                #Não deixa o cursor passar dos limites
                if cursorY < 450:
                    cursorY = 480
            #Se seta para direita, move o cursor para direita
            elif event.key == pygame.K_RIGHT:
                cenas.paginaBatalha()
                cursorX += 185
                #Não deixa o cursor passar dos limites
                if cursorX > 650:
                    cursorX = 610
            #Se seta para esquerda, move o cursor para esquerda
            elif event.key == pygame.K_LEFT:
                cenas.paginaBatalha()
                cursorX -= 185
                #Não deixa o cursor passar dos limites
                if cursorX < 250:
                    cursorX = 425
            elif event.key == pygame.K_RETURN:
                if cursorX == 425 and cursorY == 480:
                    print('Fight')
                elif cursorX == 425 and cursorY == 533:
                    print('Pokémon')
                elif cursorX == 610 and cursorY == 480:
                    print('Bag')
                elif cursorX == 610 and cursorY == 533:
                    print('Run')

    posicaoCursor(cursorX, cursorY)
    
    pygame.display.update()
