# Importando bibliotecas
import pygame
from time import sleep
# Importando módulos
from button import Button
from cursor import Cursor

pygame.init() # Iniciando pygame

# Criando a janela e mudando o nome
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pokémon')

# Importando a fonte
fonteBatalha = pygame.font.Font('joystix monospace.ttf', 25)
fontemenu = pygame.font.Font('joystix monospace.ttf', 30)
fonteDisplay = pygame.font.Font('joystix monospace.ttf', 18)

# Criando canais de som
sound_channel = pygame.mixer.Channel(0)
sound_channel.set_volume(0.1)

# Carregando os áudios
opening_theme = pygame.mixer.Sound('sounds/fireRedAbertura.wav')
battle_theme = pygame.mixer.Sound('sounds/batalha.wav')
run_theme = pygame.mixer.Sound('sounds/run.wav')
victory_theme = pygame.mixer.Sound('sounds/vitoria.wav')

beep = pygame.mixer.Sound('sounds/beep.wav')
blim = pygame.mixer.Sound('sounds/blimm.wav')
beep.set_volume(0.2) # Diminuindo o volume
blim.set_volume(0.4)


# Sprite do cursor        
cursorImage = pygame.image.load('images/cursor.png')
def blitCursor(cursorX, cursorY):
    screen.blit(cursorImage, (cursorX, cursorY))

# Iniciando variáveis importantes
turn = 1 # Define de quem é a vez de atacar
listaPokemon = [] # Lista onde serão adicionados os pokémons selecionados
listaMoves = [] # Golpes dos pokémons selecionados
dmg_health = [] # Dano dos golpes e vida dos pokémons selecionados


class Cenas:
    # Importando e ajustando as imagens
    def __init__(self):
        self.__background = pygame.image.load('images/FundoPokemon.png')
        self.__text_bar = pygame.image.load('images/text_bar.png')
        self.__fight_options = pygame.image.load('images/fgt_options.png')
        self.__health_bar1 = pygame.image.load('images/barra_1.png')
        self.__health_bar2 = pygame.image.load('images/barra_2.png')
        self.__pp_bar = pygame.image.load('images/pp_bar.png')
        
        self.__background = pygame.transform.scale(self.__background, (800,440))
        self.__text_bar = pygame.transform.scale(self.__text_bar, (800,160))
        self.__fight_options = pygame.transform.scale(self.__fight_options, (400, 160))
        self.__health_bar1 = pygame.transform.scale(self.__health_bar1, (330,100))
        self.__health_bar2 = pygame.transform.scale(self.__health_bar2, (375,126))
        self.__pp_bar = pygame.transform.scale(self.__pp_bar, (800,160))
        
        self.__pikachucostas = pygame.image.load('images/pikachuCostas.png')
        self.__pikachufrente = pygame.image.load('images/pikachuFrente.png')
        self.__charizardcostas = pygame.image.load('images/charizardCostas.png')
        self.__charizardfrente = pygame.image.load('images/charizardFrente.png')
        self.__venusaurcostas = pygame.image.load('images/venusaurCostas.png')
        self.__venusaurfrente = pygame.image.load('images/venusaurFrente.png')
        self.__blastoisecostas = pygame.image.load('images/blastoiseCostas.png')
        self.__blastoisefrente = pygame.image.load('images/blastoiseFrente.png')
        self.__mewtwocostas = pygame.image.load('images/mewtwoCostas.png')
        self.__mewtwofrente = pygame.image.load('images/mewtwoFrente.png')

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

        self.__start = pygame.image.load('images/tela_inicial.png')
        self.__start = pygame.transform.scale(self.__start, (800,600))

    # Tela inicial
    def start(self):
        start_message = fonteDisplay.render('Press any button to start', True, (255,255,255))
        screen.blit(self.__start, (0,0))
        screen.blit(start_message, (10, 560))
        pygame.display.update()
        sleep(0.3)
        start_message = fonteDisplay.render('Press any button to start', True, (0,0,255))
        screen.blit(self.__start, (0,0))
        screen.blit(start_message, (10, 560))
        pygame.display.update()
        sleep(0.3)
    
    # Tela de escolher pokémon
    def menu(self, player):        
        screen.fill((128,128,128))
        
        pygame.draw.line(screen, (0,0,0), (200,50), (200,550), 5)
        pygame.draw.line(screen, (0,0,0), (600,50), (600,550), 5)
        pygame.draw.line(screen, (0,0,0), (200,50), (600,50), 5)
        pygame.draw.line(screen, (0,0,0), (200,550), (600,550), 5)
    
        text = fontemenu.render(f'CHOOSE POKÉMON {player}', True, (0,0,0))
        pokemon1 = fontemenu.render('PIKACHU', True, (255,255,0))
        pokemon2 = fontemenu.render('CHARIZARD', True, (210,105,30))
        pokemon3 = fontemenu.render('VENUSAUR', True, (0,128,0))
        pokemon4 = fontemenu.render('BLASTOISE', True, (127,212,255))
        pokemon5 = fontemenu.render('MEWTWO', True, (255,0,255))
        #inserindo textos
        screen.blit(text, (200,5))
        screen.blit(pokemon1, (300,150))
        screen.blit(pokemon2, (300,200))
        screen.blit(pokemon3, (300,250))
        screen.blit(pokemon4, (300,300))
        screen.blit(pokemon5, (300,350))


    # Cenário inicial da batalha
    def initial(self):
        global listaPokemon

        screen.blit(self.__background, (0,0))
        screen.blit(self.__text_bar, (0,440))
        screen.blit(self.__fight_options, (400,440))
        screen.blit(self.__health_bar1, (30,30))
        screen.blit(self.__health_bar2, (415,310))
    
    # Mostrando pokémons selecionados
    def blit_pokemons(self):    
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
        
        
    # Página de golpes
    def moves(self):
        screen.blit(self.__pp_bar, (0,440))

    # Página de batalha
    def battle(self):
        screen.blit(self.__text_bar, (0,440))
        screen.blit(self.__fight_options, (400,440))

    # Quando um pokémon ataca essa função faz o golpe aparecer na tela e toca seu respectivo som
    def attacking(self, attacker, move):
        screen.blit(self.__text_bar, (0,440))
        attack = fonteBatalha.render((f'{attacker} used {move}!'), True, (255,255,255))
        screen.blit(attack, (40,480))
        pygame.display.update()
        sleep(2)
        attack_sound = pygame.mixer.Sound(f'sounds/attacks/{move}.wav')
        attack_sound.play()

    # Quando um pokémon foge, essa função faz a mensagem aparecer e toca o som de fuga
    def run(self, fujao):
        screen.blit(self.__text_bar, (0,440))
        run = fonteBatalha.render((f'{fujao} ran away!'), True, (255,255,255))
        screen.blit(run, (40,480))
        pygame.display.update()
        sound_channel.play(run_theme)
        sleep(2)
        
    # Declara o vencedor e fecha o jogo
    def winner(self, winner):
        sound_channel.play(victory_theme) # Toca a música final
        
        screen.fill((0,0,0))
        
        winner = fontemenu.render((f'{winner} is the winner!'), True, (255,255,255))
        screen.blit(winner, (120,250))
        
        pygame.display.update()
        
        sleep(5.5)
        quit()

    # Essa função faz o pokémon 1 piscar ao tomar dano
    def blink_pokemon1(self):
        for i in range(2):    
            screen.blit(self.__background, (0,150), pygame.Rect(0,150,400,290))
            pygame.display.update()
            sleep(0.2)
            cenas.blit_pokemons()
            pygame.display.update()
            sleep(0.2)
    
    # Essa função faz o pokémon 2 piscar ao tomar dano
    def blink_pokemon2(self):
        for i in range(2):    
            screen.blit(self.__background, (400,0), pygame.Rect(400,0,400,310))
            pygame.display.update()
            sleep(0.2)
            cenas.blit_pokemons()
            pygame.display.update()
            sleep(0.2) 

# Classe responsável pela vida dos pokémons
class Health:
    def __init__(self, health1, health2, listaPokemon):
        self.health1 = health1
        self.health2 = health2
        self.initialPoint1 = 588+174
        self. initialPoint2 = 161+157
        self.listaPokemon = listaPokemon
        self.red_health = pygame.image.load('images/vida_vermelha.png')
        self.black_health = pygame.image.load('images/barra_sem_vida.png')
        self.died = pygame.image.load('images/died.png')
        self.died = pygame.transform.scale(self.died, (200,200))
    
    # Faz a vida do pokemon 1 diminuir ao tomar dano
    def health1_decay(self, damage_taken, health1):
        
        self.health1 -= damage_taken
        
        damagePixels = (174 * damage_taken)//health1
        self.initialPoint1 = self.initialPoint1 - damagePixels

        if self.initialPoint1 < 588:
            self.initialPoint1 = 588

        self.red_health = pygame.transform.scale(self.red_health, (damagePixels, 10))
        screen.blit(self.red_health, (self.initialPoint1, 372))
        
        cenas.blink_pokemon1()

        return self.health1
    
    # Faz a vida do pokemon 2 diminuir ao tomar dano
    def health2_decay(self, damage_taken, health2):
        self.health2 -= damage_taken

        damagePixels = (157 * damage_taken)//health2
        self.initialPoint2 = self.initialPoint2 - damagePixels

        if self.initialPoint2 < 161:
            self.initialPoint2 = 161

        self.red_health = pygame.transform.scale(self.red_health, (damagePixels, 10))
        screen.blit(self.red_health, (self.initialPoint2, 86))
        
        cenas.blink_pokemon2()

        return self.health2
    
    # Função que checa se os pokemons estão vivos
    def check_if_is_alive(self):
        global listaPokemon
        # Se o pokémon 1 morrer, dá a vitória pro pokémon 2
        if self.initialPoint1 <= 588:
            self.black_health = pygame.transform.scale(self.black_health, (174, 10))
            screen.blit(self.black_health, (588, 372))
            screen.blit(self.died, (100,230))
            pygame.display.update()

            winner = listaPokemon[1]
            sleep(5)

            cenas.winner(winner)
        # Se o pokémon 2 morrer, dá a vitória pro pokémon 1
        elif self.initialPoint2 <= 161:
            self.black_health = pygame.transform.scale(self.black_health, (157, 10))
            screen.blit(self.black_health, (161, 86))
            screen.blit(self.died, (500,50))            
            pygame.display.update()
            
            winner = listaPokemon[0]
            sleep(5)

            cenas.winner(winner)

# Comandos da tela inicial
def comandosstart():
    global player
    # Toca música de abertura
    sound_channel.play(opening_theme, loops=-1, fade_ms=1000)
    # Loop da tela inicial
    running = True
    while running:
        cenas.start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Começa o jogo ao pressionar alguma tecla
            if event.type == pygame.KEYDOWN:
                running = False
                blim.play()
                player = 1
                cenas.menu(player)
                comandosmenu()
        
        pygame.display.update()

# Comandos da tela de seleção
def comandosmenu():
    global listaPokemon, listaMoves, turn, dmg_health, health, player

    # Tamanho do botão
    button_size = (50,25)

    # Definindo os botões
    pikachuButton = Button(button_size, (250,150))
    charizardButton = Button(button_size, (250, 200))
    venusaurButton = Button(button_size, (250, 250))
    blastoiseButton = Button(button_size, (250, 300))
    mewtwoButton = Button(button_size, (250, 350))

    # Definindo parâmetros de posição e movimento do cursor
    cursorX, cursorY = 270,150
    distanceX, distanceY = 0, 50
    limitsX, limitsY = (1000,1000), (125, 351)
    cursor = Cursor(cursorX, cursorY, distanceX, distanceY, limitsX, limitsY)

    # Loop da tela de seleção
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Ve se alguma tecla foi pressionada
            if event.type == pygame.KEYDOWN:
                beep.play()
                # Se seta para baixo, move o cursor para baixo
                if event.key == pygame.K_DOWN:
                    cenas.menu(player)
                    cursorY = cursor.move_down()

                # Se seta para cima, move o cursor para cima
                if event.key == pygame.K_UP:
                    cenas.menu(player)
                    cursorY = cursor.move_up()

                # Ao apertar enter, vê onde o cursor está e executa
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    blim.play()
                    cursor_position = [cursorX, cursorY]

                    if cursor_position in pikachuButton:
                        listaPokemon.append('pikachu')
                        listaMoves.append('THUNDER SHOCK')
                        listaMoves.append('THUNDER')
                        dmg_health.append(40), dmg_health.append(120), dmg_health.append(274)
                    
                    elif cursor_position in charizardButton:
                        listaPokemon.append('charizard')
                        listaMoves.append('EMBER')
                        listaMoves.append('FLAMETHROWER')
                        dmg_health.append(40), dmg_health.append(95), dmg_health.append(360)

                    elif cursor_position in venusaurButton:
                        listaPokemon.append('venusaur')
                        listaMoves.append('RAZOR LEAF')
                        listaMoves.append('SOLARBEAM')
                        dmg_health.append(55), dmg_health.append(120), dmg_health.append(364)

                    elif cursor_position in blastoiseButton:
                        listaPokemon.append('blastoise')
                        listaMoves.append('BITE')
                        listaMoves.append('HYDRO PUMP')
                        dmg_health.append(60), dmg_health.append(120), dmg_health.append(362)

                    elif cursor_position in mewtwoButton:
                        listaPokemon.append('mewtwo')
                        listaMoves.append('CONFUSION')
                        listaMoves.append('THUNDER')
                        dmg_health.append(50), dmg_health.append(120), dmg_health.append(416)
                    
                    player = 2
                    cenas.menu(player)
                
                # Quando os dois pokémons forem selecionados, começa a batalha
                if len(listaPokemon) == 2:
                    health = Health(dmg_health[2], dmg_health[5], listaPokemon) # Define os parâmetros da função Health
                    
                    sound_channel.play(battle_theme, loops=-1, fade_ms=1000)  # Toca a música de batalha
                    
                    screen.fill((0,0,0))
                    pygame.display.update()
                    sleep(3)
                    # Chama as funções responsáveis pela batalha
                    cenas.initial()
                    cenas.blit_pokemons()
                    comandosbattle()
        
        blitCursor(cursorX, cursorY)
        pygame.display.update()

# Comandos da tela de batalha
def comandosbattle():
    global turn, listaPokemon, winner

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

    # Verifica de quem é a vez e pergunta o que fazer
    if turn == 1:
        battleText = fonteDisplay.render(f'What will {listaPokemon[0]} do?', True, (255,255,255))
    elif turn == 2:
        battleText = fonteDisplay.render(f'What will {listaPokemon[1]} do?', True, (255,255,255))
    

    # Loop da tela de batalha
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

                # Ao apertar enter vê onde o cursor está e executa
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    cursor_position = [cursorX, cursorY]
                    
                    if cursor_position in fightButton: # Executa o botão FIGHT
                        cenas.moves()
                        comandosmoves()
                        running = False
                    elif cursor_position in bagButton: # Executa o botão BAG (não tem)
                        print('Você esqueceu a mochila em casa :P')
                    elif cursor_position in pokemonButton: # Executa o botão POKÉMON (não tem)
                        print("Não pode mudar de Pokémon :(")
                    elif cursor_position in runButton: # Executa o botão RUN
                        if turn == 1:
                            winner = listaPokemon[1]
                            fujao = listaPokemon[0]
                        elif turn == 2:
                            winner = listaPokemon[0]
                            fujao = listaPokemon[1]
                        cenas.run(fujao)
                        cenas.winner(winner)
                        
        screen.blit(battleText, (40,480))
        blitCursor(cursorX, cursorY)
        pygame.display.update()


# Comandos da tela de golpes
def comandosmoves():
    global listaMoves, turn, dmg_health, health, winner

    # Define tamanho dos botões
    button_size = (80, 80)

    # Define os botões
    move1Button = Button(button_size, (0,440))
    move2Button = Button(button_size, (0,520))

    #Posição inicial do cursor
    cursorX, cursorY = 30, 480
    distanceX, distanceY = 245, 53
    limitsX, limitsY = (30, 276),(480,534)
    cursor = Cursor(cursorX, cursorY, distanceX, distanceY, limitsX, limitsY)

    # Verifica de quem é a vez e define seus golpes
    if turn == 1:
        move1 = fonteBatalha.render(f'{listaMoves[0]}', True, (60,60,60))
        move2 = fonteBatalha.render(f'{listaMoves[1]}', True, (60,60,60))
    elif turn == 2:
        move1 = fonteBatalha.render(f'{listaMoves[2]}', True, (60,60,60))
        move2 = fonteBatalha.render(f'{listaMoves[3]}', True, (60,60,60))
    
    
    # Loop da tela de golpes
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # Movimentos do cursor
            if event.type == pygame.KEYDOWN:
                beep.play()
                if event.key == pygame.K_ESCAPE: # Ao apertar ESC, volta pra tela de batalha
                    cenas.battle()
                    comandosbattle()
                
                if event.key == pygame.K_DOWN:
                    cenas.moves()
                    cursorY = cursor.move_down()

                elif event.key == pygame.K_UP:
                    cenas.moves()
                    cursorY = cursor.move_up()

                # Ao apertar enter ve onde o cursor está e executa
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    cursor_position = [cursorX, cursorY]

                    if cursor_position in move1Button: # Executa o primeiro golpe
                        if turn == 1: # Pokémon 1 atacando
                            cenas.attacking(listaPokemon[0], listaMoves[0])
                            damage_taken = dmg_health[0]
                            
                            turn = 2 # Passa a vez pro pokémon 2
                            health.health2_decay(damage_taken, dmg_health[5])
                            health.check_if_is_alive()
                            cenas.battle()
                            comandosbattle()
                            
                        elif turn == 2: # Pokémon 2 atacando
                            cenas.attacking(listaPokemon[1], listaMoves[2])                            
                            damage_taken = dmg_health[3]

                            turn = 1 # Passa a vez pro pokémon 1
                            health.health1_decay(damage_taken, dmg_health[2])
                            health.check_if_is_alive()
                            cenas.battle()
                            comandosbattle()
                            
                    elif cursor_position in move2Button: # Executa o segundo golpe
                        if turn == 1: # Pokémon 1 atacando
                            cenas.attacking(listaPokemon[0], listaMoves[1])
                            damage_taken = dmg_health[1]
                            
                            turn = 2 # Passa a vez pro pokémon 2
                            health.health2_decay(damage_taken, dmg_health[5])
                            health.check_if_is_alive()
                            cenas.battle()
                            comandosbattle()
                            
                        elif turn == 2: # Pokémon 2 atacando
                            cenas.attacking(listaPokemon[1], listaMoves[3])
                            damage_taken = dmg_health[4]
                            
                            turn = 1 # Passa a vez pro pokémon 1
                            health.health1_decay(damage_taken, dmg_health[2])
                            health.check_if_is_alive()
                            cenas.battle()
                            comandosbattle()
            
        screen.blit(move1, (60, 480))
        screen.blit(move2, (60, 535))
        blitCursor(cursorX, cursorY)
        
        pygame.display.update()

# Classe cenas
cenas = Cenas()

# Inicia o jogo
cenas.start()
comandosstart()
