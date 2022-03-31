class Rectangle:
    def __init__(self, height, width):
        setWidth(width)
        setHeight(height)

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
            picture = '*' * self.width

            if not height == self.height - 1:
                picture += '\n'
