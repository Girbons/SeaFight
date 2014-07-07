import random


class Battlefield():

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

            if self.field[x][y]== 0:
                self.field[x][y] = 1
                self.ships += 1

    def is_hit(self, x, y):
        return self.field[x][y] == 1

shot = 0
taken = 0

battlefield = Battlefield()

def user_action():
    x = -1
    y = -1

    while x > 9 or x < 0:
        print "Insert line"
        x = int(raw_input(">  "))

    while y > 9 or y < 0:
        print "insert column"
        y = int(raw_input("> "))

    return x, y

while shot <= 50 and taken <= 30:
    x, y = user_action()
    if battlefield.is_hit(x, y):
        taken += 1
        print "SHIPS HIT"
    else:
        print "SHIPS NOT HIT "

    shot += 1


if shot <= 50:
    print "YOU HAVE LOST"

if taken == 30:
    print "YOU HAVE WON"
