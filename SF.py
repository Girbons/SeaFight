import pprint
import random


shot = 0
taken = 0


def create_battlefield():
    field = []
    ships = 0

    for i in range(10):
        line = []
        for j in range(10):
            line.append(0)
        field.append(line)

    while ships < 30:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        if field[x][y]== 0:
            field[x][y] = 1
            ships += 1
    return field


def user_action():
    x = -1
    y = -1

    while x > 9 or x < 0:
        print "Inserisci Riga"
        x = int(raw_input(">  "))

    while y > 9 or y < 0:
        print "Inserisci Colonna"
        y = int(raw_input("> "))

    return x, y


def is_taken(battlefield, x, y):
    return battlefield[x][y] == 1


    pprint.pprint(battlefield)
battlefield = create_battlefield()

while shot <= 50 and taken <= 30:
    x, y = user_action()
    if is_taken(battlefield, x, y):
        taken += 1
        print "nave colpita"
    else:
        print "nave non colpita"

    shot += 1


if shot <= 50:
    print "HAI PERSO"

if taken == 30:
    print "HAI VINTO"
