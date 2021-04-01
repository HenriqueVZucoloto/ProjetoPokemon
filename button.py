class Button:
    '''
    Propriedades:
        text,
        size,
        position,
    '''
    def __init__(self, size, position):
        self.__size = size
        self.__position = position
    
    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return self.__position

    def __contains__(self, cursor):
        x0, y0 = self.position
        dx, dy = self.size
        cursorX, cursorY = cursor

        containsX = x0 <= cursorX <= x0 + dx
        containsY = y0 <= cursorY <= y0 + dy

        return containsX and containsY
