class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        picture = ''

        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'

        for height in range(self.height):
            picture += '*' * self.width + '\n'

        return picture

    def get_amount_inside(self, shape):
        pass

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, width):
        super(Square, self).__init__(width, width)
