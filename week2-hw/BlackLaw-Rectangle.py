# Rectangle class - text based
# Allows you to change set initial data, then change the data, and show the square as text
# Because of fonts, squares will probably not show as exactly square


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width, height, hChar, vChar, cornerChar):
        """Initializes a rectangle
        Pass in the width, height, the character to used for the horizontal edge, vertical edge, and corners.
        """
        self.width = width
        self.height = height
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar

    def show(self):
        """Print the rectangle in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        """
        print()
        h = self.height
        w = self.width

        for i in range(self.height):
            edge = self.vChar if 0 < i < h - 1 else self.cornerChar
            middle = " " if 0 < i < h - 1 else self.hChar

            print(f"{edge}{middle * (w-2)}{edge}")

    def printInfo(self):
        print(
            f"Height is: {self.height}, width is: {self.width}, area is: {self.getArea()}"
        )

    def getWidth(self):
        """Returns the width of the Rectangle"""
        return self.width

    def getHeight(self):
        """Returns the height of the Rectangle"""
        return self.height

    def setHorizontalChar(self, newHChar):
        """Set a new horizontal character"""
        self.hChar = newHChar

    def setVerticalChar(self, newVChar):
        """Set a new vertical character"""
        self.vChar = newVChar

    def setCornerChar(self, newCornerChar):
        """Set a new corner character"""
        self.cornerChar = newCornerChar

    def setWidth(self, newWidth):
        """Set a new width"""
        self.width = newWidth

    def setHeight(self, newHeight):
        """Set a new height"""
        self.height = newHeight

    def getArea(self):
        """Returns the area of the rectangle"""
        return self.width * self.height


# Test code
# Create a rectangle of width 5, height 7
oRectangle1 = Rectangle(
    5, 7, "-", "|", "*"
)  # pass in size, horizonal, vertical, and edge characters
oRectangle1.show()
# print("Size is:", oSquare1.getSize(), " area is:", oSquare1.getArea())
oRectangle1.printInfo()

# Create another square of size 10, width 15
oRectangle2 = Rectangle(10, 15, "-", "|", "*")
oRectangle2.show()
# print("Size is:", oSquare2.getSize(), " area is:", oSquare2.getArea())
oRectangle2.printInfo()

# Tell the first square to modify its data
oRectangle1.setWidth(9)
oRectangle1.setHeight(4)
oRectangle1.setHorizontalChar("^")
oRectangle1.setVerticalChar("?")
oRectangle1.setCornerChar("$")
oRectangle1.show()
oRectangle1.printInfo()
print()


# Add code here to ask the user questions, and create and show a new Square based on the answers
def get_user_input_for_rectangle():
    # get rectangle width and height
    sizes = {"width": None, "height": None}
    for measurement in sizes:
        while True:
            print(f"Please input a rectangle {measurement} between 3 and 20:")
            usr_size = input("> ")
            # validate input
            if usr_size.isnumeric() and 3 < int(usr_size) < 20:
                sizes[measurement] = int(usr_size)
                break

    characters = {"corner": None, "vertical": None, "horizontal": None}

    for character in characters:
        # get character
        while True:
            print(f"Please input a {character} character")
            usr_input = input("> ")
            # validate
            if len(usr_input) == 1:
                # update dict
                characters[character] = usr_input
                break

    usr_choices = characters.copy()
    usr_choices["width"] = sizes["width"]
    usr_choices["height"] = sizes["height"]

    return usr_choices


usr_data = get_user_input_for_rectangle()
usr_rectangle = Rectangle(
    width=usr_data["width"],
    height=usr_data["height"],
    hChar=usr_data["horizontal"],
    vChar=usr_data["vertical"],
    cornerChar=usr_data["corner"],
)
usr_rectangle.show()
usr_rectangle.printInfo()
