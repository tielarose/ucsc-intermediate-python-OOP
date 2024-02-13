# Square class - text based
# Allows you to change set initial data, then change the data, and show the square as text
# Because of fonts, squares will probably not show as exactly square


class Square:
    """Represents a square"""

    def __init__(self, size, hChar, vChar, cornerChar):
        """Initializes a square
        Pass in the size, the character to used for the horizontal edge, vertical edge, and corners.
        """
        self.size = size
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar

    def show(self):
        """Print the square in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        """
        print()
        n = self.size

        for i in range(n):
            edge = self.vChar if 0 < i < n - 1 else self.cornerChar
            middle = " " if 0 < i < n - 1 else self.hChar

            print(f"{edge}{middle * (n-2)}{edge}")

    def getSize(self):
        """Returns the size of an edge of the Square"""
        return self.size

    def setHorizontalChar(self, newHChar):
        """Set a new horizontal character"""
        self.hChar = newHChar

    def setVerticalChar(self, newVChar):
        """Set a new vertical character"""
        self.vChar = newVChar

    def setCornerChar(self, newCornerChar):
        """Set a new corner character"""
        self.cornerChar = newCornerChar

    # Must add 2 additional methods: setSize and getArea
    def setSize(self, newSize):
        """Set a new size"""
        self.size = newSize

    def getArea(self):
        """Returns the area of the square"""
        return self.size * self.size


# Test code
# Create a square of size 5
oSquare1 = Square(
    5, "-", "|", "*"
)  # pass in size, horizonal, vertical, and edge characters
oSquare1.show()
print("Size is:", oSquare1.getSize(), " area is:", oSquare1.getArea())

# Create another square of size 10
oSquare2 = Square(10, "-", "|", "*")
oSquare2.show()
print("Size is:", oSquare2.getSize(), " area is:", oSquare2.getArea())

# Tell the first square to modify its data
oSquare1.setSize(7)
oSquare1.setHorizontalChar("^")
oSquare1.setVerticalChar("?")
oSquare1.setCornerChar("$")
oSquare1.show()
print("Size is:", oSquare1.getSize(), " area is:", oSquare1.getArea())
print()


# Add code here to ask the user questions, and create and show a new Square based on the answers
def get_user_input_for_square():
    # get square size
    print("Please input a square size less than 20:")
    usr_size = input("> ")

    # validate input
    while not usr_size.isnumeric() or int(usr_size) > 20:
        print("Invalid input. Square size must be a number less than 20.")
        print("Please input a square size")
        usr_size = input("> ")

    characters = {"corner": None, "vertical": None, "horizontal": None}

    for character in characters:
        # get character
        print(f"Please input a {character} character")
        usr_input = input("> ")

        # validate
        while len(usr_input) > 1:
            print("Invalid input. Please input one character only")
            usr_input = input("> ")

        # update dict
        characters[character] = usr_input

    usr_choices = characters.copy()
    usr_choices["size"] = int(usr_size)

    print(usr_choices)
    return usr_choices


# ******* variable unpacking to make this more elegant??
# size, corner, vertical, horizontal = get_user_input_for_square()
usr_data = get_user_input_for_square()
usr_square = Square(
    size=usr_data["size"],
    hChar=usr_data["horizontal"],
    vChar=usr_data["vertical"],
    cornerChar=usr_data["corner"],
)
usr_square.show()
print(f"Size is: {usr_square.getSize()}, area is: {usr_square.getArea()}")
