import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for key, value in kwargs.items():
            for balls in range(value):
                self.contents.append(key)

    def draw(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents

        for number in range(number_of_balls):
            index = random.randint(0, len(self.contents) - 1)
            del self.contents[index]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    N = num_experiments
    M = 0
    num_balls = 0

    hat.draw(num_balls_drawn)

    # number of balls to draw
    for key, value in expected_balls.items():
        num_balls += value

    # experiments
    for iter in range(num_experiments):
        for draw in range(num_balls):
            if hat.contents[random.randint(0, len(hat.contents) - 1)] in expected_balls.keys():
                M += 1

        if M == num_balls:
            probability = M / N

        M = 0

    return probability


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
