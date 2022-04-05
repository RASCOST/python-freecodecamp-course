import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for key, value in kwargs.items():
            for balls in range(value):
                self.contents.append(key)

    def draw(self, number_of_balls):
        balls = []

        if number_of_balls > len(self.contents):
            return self.contents

        for number in range(number_of_balls):
            index = random.randint(0, len(self.contents) - 1)
            balls.append(self.contents[index])
            del self.contents[index]

        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    N = num_experiments
    M = 0

    for iter in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        balls = temp_hat.draw(num_balls_drawn)
        expected = expected_balls
        expected = expected.fromkeys(expected, 0)
        match = False

        for index in range(len(balls)):
            if balls[index] in expected:
                expected[balls[index]] += 1

        for key, value in expected_balls.items():
            if expected[key] >= value:
                match = True
            else:
                match = False
                break

        if match:
            M += 1

    probability = M / N

    return probability
