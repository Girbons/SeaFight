__author__ = 'alessandro'

import random


class Battlefield(object):

    def __init__(self,):

        self.field = []
        self.ships = 0

        for i in range(10):
            line = []
            for j in range(10):
                line.append(0)
            self.field.append(line)

        while self.ships < 30:
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            if self.field[x][y] == 0:
                self.field[x][y] = 1
                self.ships += 1

    def is_hit(self, x, y):
        return self.field[x][y]
