class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shape = "Rectangle"

    def __str__(self):
        return self.shape + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        output = ""
        for i in range(self.height):
            output += "*" * self.width + "\n"
        return output

    def get_amount_inside(self, shape):
        area_self = self.get_area()
        area_shape = shape.get_area()
        amount_inside = int(area_self / area_shape)
        return amount_inside


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        self.shape = "Square"

    def __str__(self):
        return self.shape + "(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side
        