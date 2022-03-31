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

    def get_perimeter(self)
        return (2 * self.width + 2 * self.height)
