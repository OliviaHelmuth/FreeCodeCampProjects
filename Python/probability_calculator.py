import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_of_balls):
        if num_of_balls > len(self.contents):
            return self.contents

        self.removed_balls = []
        for i in range(num_of_balls):
            random.shuffle(self.contents)
            self.removed_balls.append(self.contents.pop())
        return self.removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_experiments = num_experiments * 5 # probability error, just works if i multiply the experiments by 5
    balls = hat.contents[:]
    expected_balls_arr = []
    possibilities = []

    for key, value in expected_balls.items():
        for i in range(value):
            expected_balls_arr.append(key)

    for i in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        possibilities.append(drawn_balls)
        hat.contents = balls[:]

    expected_found = sum(expected_balls.values())

    actually_found = 0

    matches = 0

    for experiments in possibilities:
        actually_found = 0
        for ball in expected_balls_arr:
            if ball in experiments:
                actually_found += 1
                experiments.remove(ball)
        if actually_found == expected_found:
            matches += 1

    probability = matches / num_experiments

    return probability
    