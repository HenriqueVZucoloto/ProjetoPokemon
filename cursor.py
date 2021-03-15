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
    def __init__(self, cursorX,cursorY, distanceX, distanceY, limitsX, limitsY):
        self.__cursorX = cursorX
        self.__cursorY = cursorY
        self.__distanceX = distanceX
        self.__distanceY = distanceY
        self.__limitsX = limitsX
        self.__limitsY = limitsY
    
    def move_down(self):
        newcursorY = self.__cursorY + self.__distanceY
        if newcursorY in range(self.__limitsY[0], self.__limitsY[1]):
            self.__cursorY = newcursorY
        else:
            self.__cursorY = self.__cursorY - self.__distanceY
        return self.__cursorY

    def move_up(self):
        newcursorY = self.__cursorY - self.__distanceY
        if newcursorY in range(self.__limitsY[0], self.__limitsY[1]):
            self.__cursorY = newcursorY
        else:
            self.__cursorY = self.__cursorY + self.__distanceY
        return self.__cursorY
        
    def move_right(self):
        newcursorX = self.__cursorX + self.__distanceX
        if newcursorX in range(self.__limitsX[0], self.__limitsX[1]):
            self.__cursorX = newcursorX
        else:
            self.__cursorX = self.__cursorX - self.__distanceX
        return self.__cursorX
    
    def move_left(self):
        newcursorX = self.__cursorX - self.__distanceX
        if newcursorX in range(self.__limitsX[0], self.__limitsX[1]):
            self.__cursorX = newcursorX
        else:
            self.__cursorX = self.__cursorX + self.__distanceX
        return self.__cursorX
