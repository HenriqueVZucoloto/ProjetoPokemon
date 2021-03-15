import pygame
from button import Button
from cursor import Cursor

pygame.init()

# Cria a janela e muda o nome
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('HOJE TEM GOL DO RIBAMAR')

# Importa a fonte
font = pygame.font.Font('joystix monospace.ttf', 20)

class Cenas:
    # Importa e ajusta as imagens
    def __init__(self):
        self.__background = pygame.image.load('FundoPokemon.png')
        self.__text_bar = pygame.image.load('text_bar.png')
        self.__fight_options = pygame.image.load('fgt_options.png')
        self.__health_bar1 = pygame.image.load('barra_1.png')
        self.__health_bar2 = pygame.image.load('barra_2.png')
        self.__pp_bar = pygame.image.load('pp_bar.png')
    
        self.__background = pygame.transform.scale(self.__background, (800,440))
        self.__text_bar = pygame.transform.scale(self.__text_bar, (800,160))
        self.__fight_options = pygame.transform.scale(self.__fight_options, (400, 160))
        self.__health_bar1 = pygame.transform.scale(self.__health_bar1, (330,100))
        self.__health_bar2 = pygame.transform.scale(self.__health_bar2, (375,126))
        self.__pp_bar = pygame.transform.scale(self.__pp_bar, (800,160))

    # Cria o cenário inicial da batalha
    def initial(self):
        screen.blit(self.__background, (0,0))
        screen.blit(self.__text_bar, (0,440))
        screen.blit(self.__fight_options, (400,440))
        screen.blit(self.__health_bar1, (30,30))
        screen.blit(self.__health_bar2, (415,310))
        
        #pygame.mixer.music.play(0)  # Toca a música de batalha
        
    # Abre a página de golpes
    def moves(self):
        screen.blit(self.__pp_bar, (0,440))


    # Abre a página de batalha
    def battle(self):
        screen.blit(self.__text_bar, (0,440))
        screen.blit(self.__fight_options, (400,440))

# Importa e printa o cursor        
cursorImage = pygame.image.load('cursor.png')
def blitCursor(cursorX, cursorY):
    screen.blit(cursorImage, (cursorX, cursorY))

class Comandos:
    # Ativa os comandos da pagina de batalha
    def battle(self):       
        # Define tamanho e texto dos botões
        button_size = (200, 80)
        text = ''

        # Define os botões
        fightButton = Button(text, button_size, (400,440))
        bagButton = Button(text, button_size, (600,440))
        pokemonButton = Button(text, button_size, (400,520))
        runButton = Button(text, button_size, (600,520))

        # Definindo parâmetros de posição e movimento do cursor
        cursorX, cursorY = 425, 480
        distanceX, distanceY = 185, 53
        limitsX, limitsY = (425, 611), (480, 534)
        cursor = Cursor(cursorX, cursorY, distanceX, distanceY, limitsX, limitsY)

        # Loop da cena de batalha
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                # Movimentos do cursor
                if event.type == pygame.KEYDOWN:
                    beep.play()
                    if event.key == pygame.K_DOWN:
                        cenas.battle()
                        cursorY = cursor.move_down()
                        
                    elif event.key == pygame.K_UP:
                        cenas.battle()
                        cursorY = cursor.move_up()
                    
                    elif event.key == pygame.K_RIGHT:
                        cenas.battle()
                        cursorX = cursor.move_right()
                    
                    elif event.key == pygame.K_LEFT:
                        cenas.battle()
                        cursorX = cursor.move_left()

                    # Ao apertar enter:
                    if event.key == pygame.K_RETURN:
                        # Vê onde o cursor está e executa
                        cursor_position = [cursorX, cursorY]
                        if cursor_position in fightButton:
                            print('fight')
                            cenas.moves()
                            comandos.moves()
                            running = False
                        elif cursor_position in bagButton:
                            print('bag')
                        elif cursor_position in pokemonButton:
                            print('pokemon')
                        elif cursor_position in runButton:
                            print('run') 
            
            blitCursor(cursorX, cursorY)
            pygame.display.update()
            

    def moves(self):
        # Define tamanho e texto dos botões
        button_size = (80, 80)
        text = ''

        # Define os botões
        move1Button = Button(text, button_size, (0,440))
        move2Button = Button(text, button_size, (267,440))
        move3Button = Button(text, button_size, (0,520))
        move4Button = Button(text, button_size, (267,520))

        #Posição inicial do cursor
        cursorX, cursorY = 30, 480
        distanceX, distanceY = 245, 53
        limitsX, limitsY = (30, 276),(480,534)
        cursor = Cursor(cursorX, cursorY, distanceX, distanceY, limitsX, limitsY)

        # Loop da cena de batalha
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                # Movimentos do cursor
                if event.type == pygame.KEYDOWN:
                    beep.play()
                    if event.key == pygame.K_ESCAPE:
                        cenas.battle()
                    
                    if event.key == pygame.K_DOWN:
                        cenas.moves()
                        cursorY = cursor.move_down()

                    elif event.key == pygame.K_UP:
                        cenas.moves()
                        cursorY = cursor.move_up()

                    elif event.key == pygame.K_RIGHT:
                        cenas.moves()
                        cursorX = cursor.move_right()

                    elif event.key == pygame.K_LEFT:
                        cenas.moves()
                        cursorX = cursor.move_left()

                    # Ao apertar enter
                    if event.key == pygame.K_RETURN:
                        # Ve onde o cursor está e executa
                        cursor_position = [cursorX, cursorY]
                        if cursor_position in move1Button:
                            print('move 1')
                        elif cursor_position in move2Button:
                            print('move 2')
                        elif cursor_position in move3Button:
                            print('move 3')
                        elif cursor_position in move4Button:
                            print('move 4') 
            
            blitCursor(cursorX, cursorY)
            pygame.display.update()


            


# Carrega os áudios
pygame.mixer.music.load('batalha.wav')
pygame.mixer.music.set_volume(0.3)
beep = pygame.mixer.Sound('beep.wav')

cenas = Cenas()
comandos = Comandos()


cenas.initial()
comandos.battle()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()

pygame.quit()
