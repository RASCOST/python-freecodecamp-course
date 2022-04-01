class Hat:
    def __init__(**kwargs):
        self.contents = []

        for key, value in kwargs:
            for balls in range(value):
                self.contents.append(key)

    def draw(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents

        for number in range(number_of_balls):
            index = random.randint(0, len(self.contents))
            del self.content[index]
