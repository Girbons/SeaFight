from model import Player, Game
import sys



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



players_number = -1
players = []




# My game

print "How many players ?"
try:
    players_number = int(raw_input("> "))
except:
    print "you must insert only number"
    sys.exit(1)



for i in range(players_number):
    name = raw_input("Player %s name: " % (i + 1))
    players.append(Player(name))

game = Game(players)

while game.shot <= 40:

    print "Current player %s " % game.current_player()
    x, y = user_action()

    if game.fire(game.current_player(), x, y) == 1:
        print "player %s hit an enemy ship" % game.current_player()

    elif game.fire(game.current_player(), x, y) == 0:
        print "player %s didn't hit an enemy ship " % game.current_player()


    elif game.fire(game.current_player(), x, y) == 2:
        print "Ships already hit"

    game.next_turn()

print "The winner is Player %s!" % game.winner()
