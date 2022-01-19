class Rectangle:

    # initializing object
    # Parameters (int, int)
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.unit = "ft"

    # prints width of rectangle
    def get_width(self):
        print(self.width + self.unit)

    # prints length of rectangle
    def get_length(self):
        print(self.length + self.unit)

    # Changes the width of the rectangle
    def set_width(self, width):
        self.width = width

    # Changes the length of the rectangle
    def set_length(self, length):
        self.length = length

    # Calculates perm of the rectangle
    def get_perimeter(self):
        print("The perimeter of this rectangle is " + str((2 * self.length + 2 * self.width)) + self.unit)

    # Calculates area of the rectangle
    def get_area(self):
        print("The area of this rectangle is " + str(self.length * self.width) + self.unit)
