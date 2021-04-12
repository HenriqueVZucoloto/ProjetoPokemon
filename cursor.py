class Cursor:
    '''
    Propriedades:
        cursorX,
        cursorY,
        distanceX
        distanceY,
        limitsX,
        limitsY
    '''
    def __init__(self, cursorX,cursorY, distanceX, distanceY, limitsX, limitsY): # Parâmetros de posição, movimento e limite do cursor
        self.__initialY = cursorY
        self.__cursorX = cursorX
        self.__cursorY = cursorY
        self.__distanceX = distanceX
        self.__distanceY = distanceY
        self.__limitsX = limitsX
        self.__limitsY = limitsY
    
    def move_down(self): # Move o cursor pra baixo
        newcursorY = self.__cursorY + self.__distanceY
        if newcursorY in range(self.__limitsY[0], self.__limitsY[1]):
            self.__cursorY = newcursorY
        else:
            self.__cursorY = self.__initialY
        return self.__cursorY

    def move_up(self): # Move o cursor pra cima
        newcursorY = self.__cursorY - self.__distanceY
        if newcursorY in range(self.__limitsY[0], self.__limitsY[1]):
            self.__cursorY = newcursorY
        else:
            self.__cursorY = self.__limitsY[1]-1
        return self.__cursorY
        
    def move_right(self): # Move o cursor pra direita
        newcursorX = self.__cursorX + self.__distanceX
        if newcursorX in range(self.__limitsX[0], self.__limitsX[1]):
            self.__cursorX = newcursorX
        else:
            self.__cursorX = self.__cursorX - self.__distanceX
        return self.__cursorX
    
    def move_left(self): # Move o cursor pra esquerda
        newcursorX = self.__cursorX - self.__distanceX
        if newcursorX in range(self.__limitsX[0], self.__limitsX[1]):
            self.__cursorX = newcursorX
        else:
            self.__cursorX = self.__cursorX + self.__distanceX
        return self.__cursorX
