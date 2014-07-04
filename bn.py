import pprint
import random

shot=0
taken=0
while shot==50 || taken==30:
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

        print "Inserisci Riga"
        x = raw_input(" ")
        print "Inserisci Colonna"
        y = raw_input(" ")

        x = int(x)
        y = int(y)
        if battlefield[x][y]==1:
            print "nave colpita"
            
        else:
            print "nave non colpita"

    action = user_action(battlefield)

    pprint.pprint(action)
    colpi =+ 1
    #pprint.pprint(battlefield)



