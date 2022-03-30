class Rectangle:
    def __init__(self, height, width):
        setWidth(width)
        setHeight(height)

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getArea(self):
        return self.width * self.height
