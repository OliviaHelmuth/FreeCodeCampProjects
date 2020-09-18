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


def experiment(hat, num_balls_drawn, num_experiments):
    balls = hat.contents[:]
    possibilities = []

    for i in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        possibilities.append(drawn_balls)
        hat.contents = balls[:]


hat1 = Hat(yellow=2, blue=2, green=2)
# print(hat1.draw(4))
experiment(hat1, 2, 2)
