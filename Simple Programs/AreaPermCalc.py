# Simple Area/Perimeter Calculator for Rectangle


class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # prints width of shape

    def get_width(self):
        return self.width

    # prints length of shape
    def get_length(self):
        return self.length

    # Changes the width of the shape
    def set_width(self, width):
        self.width = width

    # Changes the length of the shape
    def set_length(self, length):
        self.length = length

    # Calculates perm of the shape
    def get_perimeter(self):
        print("The perimeter of this shape is " + str(2 * self.length + 2 * self.width))

    # Calculates area of the shape
    def get_area(self):
        print("The area of this shape is " + str(self.length * self.width))


# Practicing inheritance


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)


# Starts the calculator
while True:
    print("Calculate a rectangle")

    while True:
        # Asks user to input length and width that must be an integer
        try:
            length = int(input("Enter a length value: "))
            width = int(input("Enter a width value: "))
        except ValueError:
            print("Invalid number.")
            continue
        else:
            break
    rect1 = Rectangle(length, width)
    # Asks the user to choose from a list of functions to be done on the rectangle
    print("1: Get length")
    print("2: Get width")
    print("3: Set length")
    print("4: Set width")
    print("5: Perimeter")
    print("6: Area")
    print("7: Quit")
    while True:
        try:
            ans = int(input("Choose the number that corresponds to the function: "))
        except ValueError:
            print("Invalid Number")
        else:
            # if else statements based on what number the user chose
            if ans == 1:
                rect1.get_length()
            elif ans == 2:
                rect1.get_width()
            elif ans == 3:
                try:
                    length = int(input("Enter a number to set length: "))
                except ValueError:
                    print("Invalid number.")
                else:
                    rect1.set_length(length)
                    print(
                        "You have set the length the rectangle to "
                        + str(rect1.get_length())
                    )
            elif ans == 4:
                try:
                    width = int(input("Enter a number to set the width: "))
                except ValueError:
                    print("Invalid number.")
                else:
                    rect1.set_width(width)
                    print(
                        "You have set the width of the rectangle to "
                        + str(rect1.get_width())
                    )
            elif ans == 5:
                rect1.get_perimeter()
            elif ans == 6:
                rect1.get_area()
            # breaks while loop and exits the program
            elif ans == 7:
                break
