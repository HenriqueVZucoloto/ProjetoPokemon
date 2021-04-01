import pygame
from button import Button
from cursor import Cursor

pygame.init()

# Cria a janela e muda o nome
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('HOJE TEM GOL DO RIBAMAR')

# Importa a fonte
fonteBatalha = pygame.font.Font('joystix monospace.ttf', 25)
fontemenu = pygame.font.Font('joystix monospace.ttf', 30)

# Carrega os áudios
pygame.mixer.music.load('batalha.wav')
pygame.mixer.music.set_volume(0.3)
beep = pygame.mixer.Sound('beep.wav')
blim = pygame.mixer.Sound('blimm.wav')

# Importa e printa o cursor        
cursorImage = pygame.image.load('cursor.png')
def blitCursor(cursorX, cursorY):
    screen.blit(cursorImage, (cursorX, cursorY))



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
        
        self.__pikachucostas = pygame.image.load('pikachuCostas.png')
        self.__pikachufrente = pygame.image.load('pikachuFrente.png')
        self.__charizardcostas = pygame.image.load('charizardCostas.png')
        self.__charizardfrente = pygame.image.load('charizardFrente.png')
        self.__venusaurcostas = pygame.image.load('venusaurCostas.png')
        self.__venusaurfrente = pygame.image.load('venusaurFrente.png')
        self.__blastoisecostas = pygame.image.load('blastoiseCostas.png')
        self.__blastoisefrente = pygame.image.load('blastoiseFrente.png')
        self.__mewtwocostas = pygame.image.load('mewtwoCostas.png')
        self.__mewtwofrente = pygame.image.load('mewtwoFrente.png')

        self.__pikachucostas = pygame.transform.scale(self.__pikachucostas, (300,300))
        self.__pikachufrente = pygame.transform.scale(self.__pikachufrente, (300,300))
        self.__charizardcostas = pygame.transform.scale(self.__charizardcostas, (300,300))
        self.__charizardfrente = pygame.transform.scale(self.__charizardfrente, (300,300))
        self.__venusaurcostas = pygame.transform.scale(self.__venusaurcostas, (300,300))
        self.__venusaurfrente = pygame.transform.scale(self.__venusaurfrente, (300,300))
        self.__blastoisecostas = pygame.transform.scale(self.__blastoisecostas, (300,300))
        self.__blastoisefrente = pygame.transform.scale(self.__blastoisefrente, (300,300))
        self.__mewtwocostas = pygame.transform.scale(self.__mewtwocostas, (300,300))
        self.__mewtwofrente = pygame.transform.scale(self.__mewtwofrente, (300,300))

    # Tela de escolher pokémon
    def menu(self):
        screen.fill((128,128,128))
        
        pygame.draw.line(screen, (0,0,0), (200,50), (200,550), 5)
        pygame.draw.line(screen, (0,0,0), (600,50), (600,550), 5)
        pygame.draw.line(screen, (0,0,0), (200,50), (600,50), 5)
        pygame.draw.line(screen, (0,0,0), (200,550), (600,550), 5)
    
        texto = fontemenu.render('ESCOLHA SEU POKÉMON', True, (0,0,0))
        pokemon1 = fontemenu.render('PIKACHU', True, (255,255,0))
        pokemon2 = fontemenu.render('CHARIZARD', True, (210,105,30))
        pokemon3 = fontemenu.render('VENUSAUR', True, (0,128,0))
        pokemon4 = fontemenu.render('BLASTOISE', True, (127,212,255))
        pokemon5 = fontemenu.render('MEWTWO', True, (255,0,255))
        #inserindo textos
        screen.blit(texto, (160,5))
        screen.blit(pokemon1, (300,150))
        screen.blit(pokemon2, (300,200))
        screen.blit(pokemon3, (300,250))
        screen.blit(pokemon4, (300,300))
        screen.blit(pokemon5, (300,350))


    # Cria o cenário inicial da batalha
    def initial(self):
        global listaPokemon
        screen.blit(self.__background, (0,0))
        screen.blit(self.__text_bar, (0,440))
        screen.blit(self.__fight_options, (400,440))
        screen.blit(self.__health_bar1, (30,30))
        screen.blit(self.__health_bar2, (415,310))
        if listaPokemon[0] == 'pikachu':
            screen.blit(self.__pikachucostas, (50,172))
            pikachuNome = fonteBatalha.render('PIKACHU', True, (60,60,60))
            screen.blit(pikachuNome, (470,325))
        if listaPokemon[1] == 'pikachu':
            screen.blit(self.__pikachufrente, (450,10))
            pikachuNome = fonteBatalha.render('PIKACHU', True, (60,60,60))
            screen.blit(pikachuNome, (50,40))
        if listaPokemon[0] == 'charizard':
            screen.blit(self.__charizardcostas, (50,158))
            charizardNome = fonteBatalha.render('CHARIZARD', True, (60,60,60))
            screen.blit(charizardNome, (470,325))
        if listaPokemon[1] == 'charizard':
            screen.blit(self.__charizardfrente, (450,10))
            charizardNome = fonteBatalha.render('CHARIZARD', True, (60,60,60))
            screen.blit(charizardNome, (50,40))
        if listaPokemon[0] == 'venusaur':
            screen.blit(self.__venusaurcostas, (50,186))
            venusaurNome = fonteBatalha.render('VENUSAUR', True, (60,60,60))
            screen.blit(venusaurNome, (470,325))
        if listaPokemon[1] == 'venusaur':
            screen.blit(self.__venusaurfrente, (450,10))
            venusaurNome = fonteBatalha.render('VENUSAUR', True, (60,60,60))
            screen.blit(venusaurNome, (50,40))
        if listaPokemon[0] == 'blastoise':
            screen.blit(self.__blastoisecostas, (50,186))
            blastoiseNome = fonteBatalha.render('BLASTOISE', True, (60,60,60))
            screen.blit(blastoiseNome, (470,325))
        if listaPokemon[1] == 'blastoise':
            screen.blit(self.__blastoisefrente, (450,10))
            blastoiseNome = fonteBatalha.render('BLASTOISE', True, (60,60,60))
            screen.blit(blastoiseNome, (50,40))
        if listaPokemon[0] == 'mewtwo':
            screen.blit(self.__mewtwocostas, (50,144))
            mewtwoNome = fonteBatalha.render('MEWTWO', True, (60,60,60))
            screen.blit(mewtwoNome, (470,325))
        if listaPokemon[1] == 'mewtwo':
            screen.blit(self.__mewtwofrente, (420,5))
            mewtwoNome = fonteBatalha.render('MEWTWO', True, (60,60,60))
            screen.blit(mewtwoNome, (50,40))
        
        
        #pygame.mixer.music.play(0)  # Toca a música de batalha
        
    # Abre a página de golpes
    def moves(self):
        screen.blit(self.__pp_bar, (0,440))

    # Abre a página de batalha
    def battle(self):
        screen.blit(self.__text_bar, (0,440))
        screen.blit(self.__fight_options, (400,440))

class Comandos:
    # Comandos do menu
    def menu(self):
        global listaPokemon

        #Tamanho do botão
        button_size = (50,25)

        #Definindo os botões
        pikachuButton = Button(button_size, (250,150))
        charizardButton = Button(button_size, (250, 200))
        venusaurButton = Button(button_size, (250, 250))
        blastoiseButton = Button(button_size, (250, 300))
        mewtwoButton = Button(button_size, (250, 350))
    
        # Definindo parâmetros de posição e movimento do cursor
        cursorX, cursorY = 270,150
        distanceX, distanceY = 0, 50
        limitsX, limitsY = (1000,1000), (125, 400)
        cursor = Cursor(cursorX, cursorY, distanceX, distanceY, limitsX, limitsY)
        
        listaPokemon = []

        #Loop da cena escolher
        escolhendo = True
        while escolhendo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    escolhendo = False

                #Ve se alguma tecla foi pressionada
                if event.type == pygame.KEYDOWN:
                    beep.play()
                    #Se seta para baixo, move o cursor para baixo
                    if event.key == pygame.K_DOWN:
                        cenas.menu()
                        cursorY = cursor.move_down()

                    #Se seta para cima, move o cursor para cima
                    if event.key == pygame.K_UP:
                        cenas.menu()
                        cursorY = cursor.move_up()

                    #Apertar enter
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        blim.play()
                    # Vê onde o cursor está e executa
                        cursor_position = [cursorX, cursorY]
                        if cursor_position in pikachuButton:
                            listaPokemon.append('pikachu')
                        elif cursor_position in charizardButton:
                            listaPokemon.append('charizard')
                        elif cursor_position in venusaurButton:
                            listaPokemon.append('venusaur')
                        elif cursor_position in blastoiseButton:
                            listaPokemon.append('blastoise')
                        elif cursor_position in mewtwoButton:
                            listaPokemon.append('mewtwo')
                    
                    if len(listaPokemon) == 2:
                        print(listaPokemon)
                        cenas.initial()
                        comandos.battle()
                        
            blitCursor(cursorX, cursorY)
            pygame.display.update()

    # Ativa os comandos da pagina de batalha
    def battle(self):       
        # Define tamanho dos botões
        button_size = (200, 80)

        # Define os botões
        fightButton = Button(button_size, (400,440))
        bagButton = Button(button_size, (600,440))
        pokemonButton = Button(button_size, (400,520))
        runButton = Button(button_size, (600,520))

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
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
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

        # Define os botões
        move1Button = Button(button_size, (0,440))
        move2Button = Button(button_size, (0,520))

        #Posição inicial do cursor
        cursorX, cursorY = 30, 480
        distanceX, distanceY = 245, 53
        limitsX, limitsY = (30, 276),(480,534)
        cursor = Cursor(cursorX, cursorY, distanceX, distanceY, limitsX, limitsY)

        # Loop da cena de golpes
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
                        comandos.battle()
                    
                    if event.key == pygame.K_DOWN:
                        cenas.moves()
                        cursorY = cursor.move_down()

                    elif event.key == pygame.K_UP:
                        cenas.moves()
                        cursorY = cursor.move_up()

                    # Ao apertar enter
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        # Ve onde o cursor está e executa
                        cursor_position = [cursorX, cursorY]
                        if cursor_position in move1Button:
                            print('move 1')
                        elif cursor_position in move2Button:
                            print('move 2')

            blitCursor(cursorX, cursorY)
            pygame.display.update()



cenas = Cenas()
comandos = Comandos()


cenas.menu()
comandos.menu()


# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()

pygame.quit()
