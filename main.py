import pygame
pygame.init()
class Janela:
    __largura = 0 #largura
    __altura = 0 #altura
    __color = (0, 0, 0) #cor

    def __init__(self, largura, altura): #construtor
        self.__largura = largura
        self.__altura = altura

    def tamanhoJanela(self): #retorna tamanho da tela
        return (self.__largura, self.__altura)

    def returnCor(self): #retorna a cor da janela
        return self.__color

w = Janela(800, 600) #cria objeto janela com dimensões 500x500
win = pygame.display.set_mode(w.tamanhoJanela()) #inicializa a janela do jogo
