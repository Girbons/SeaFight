from model import Battlefield


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
