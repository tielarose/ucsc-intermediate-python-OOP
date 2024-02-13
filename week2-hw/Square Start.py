# Square class - text based
# Allows you to change set initial data, then change the data, and show the square as text
# Because of fonts, squares will probably not show as exactly square

class Square():
    """Represents a square
    """

    def __init__(self, size, hChar, vChar, cornerChar):
        ''' Initializes a square
        Pass in the size, the character to used for the horizontal edge, vertical edge, and corners.
        '''
        self.size = size
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar

    def show(self):
        ''' Print the square in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        '''       
        print()
        print('This line should be replaced with lines to draw this Square.')

    def getSize(self):
        ''' Returns the size of an edge of the Square '''
        pass

    def setHorizontalChar(self, newHChar):
        ''' Set a new horizontal character '''
        pass
        
    def setVerticalChar(self, newVChar):
        ''' Set a new vertical character '''
        pass

    def setCornerChar(self, newCornerChar):
        ''' Set a new corner character '''
        pass

    # Must add 2 additional methods: setSize and getArea


# Test code
# Create a square of size 5
oSquare1 = Square(5, '-', '|', '*')  # pass in size, horizonal, vertical, and edge characters
oSquare1.show()
print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())

# Create another square of size 10
oSquare2 = Square(10, '-', '|', '*')
oSquare2.show()
print('Size is:', oSquare2.getSize(), " area is:", oSquare2.getArea())

# Tell the first square to modify its data
oSquare1.setSize(7)
oSquare1.setHorizontalChar('^')
oSquare1.setVerticalChar('?')
oSquare1.setCornerChar('$')
oSquare1.show()
print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())
print()


# Add code here to ask the user questions, and create and show a new Square based on the answers
