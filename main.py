import pygame
pygame.init()

#Cria a janela
janela = pygame.display.set_mode((800,600)) #inicializa a janela do jogo

#Muda o nome
pygame.display.set_caption('HOJE TEM GOL DO RIBAMAR')

class Cenas:
    #Cria o cenário da batalha
    def cenarioInicialBatalha(self):
        #Carrega as imagens
        self.fundoBatalha = pygame.image.load('FundoPokemon.png')
        self.caixaTexto = pygame.image.load('text_bar.png')
        self.opcoesBatalha = pygame.image.load('fgt_options.png')
        self.barra1 = pygame.image.load('barra_1.png')
        self.barra2 = pygame.image.load('barra_2.png')
        
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
        self.caixaGolpes = pygame.image.load('pp_bar.png')
        self.caixaGolpes = pygame.transform.scale(self.caixaGolpes, (800,160))
        janela.blit(self.caixaGolpes, (0,440))

cenas = Cenas()
cenas.cenarioInicialBatalha()
cenas.paginaGolpes()


#Loop do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    pygame.display.update()
