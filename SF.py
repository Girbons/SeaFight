import pprint
import random

shot=0
taken=0


while shot <= 10 or taken <= 30:
    def create_battlefield():
        field = []
        for i in range(10):
            line = []
            for j in range(10):
                line.append(0)
            field.append(line)

        ships=0

        while ships<30:
            x = random.randint(0,9)
            y = random.randint(0,9)

            if field[x][y]==0:
                field[x][y] = 1
                ships +=1
        return field


    battlefield = create_battlefield()

    def user_action(battlefield):
        while True:
            print "Inserisci Riga"
            x = raw_input("> ")
            if x > 10:
                break

        while True:
            print "Inserisci Colonna"
            y = raw_input("> ")
            if y > 10:
                break

            x = int(x)
            y = int(y)
            if battlefield[x][y]==1:
                print "nave colpita"

            else:
                print "nave non colpita"

    action = user_action(battlefield)

    pprint.pprint(action)
    shot=shot+1

    #pprint.pprint(battlefield)
if shot==10:
    print "You have lost"

if taken==30:
    print "You have win"