class Hat:
    def __init__(**kwargs):
        self.contents = []

        for key, value in kwargs:
            for balls in range(value):
                self.contents.append(key)
