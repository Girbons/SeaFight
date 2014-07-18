from model import Player, Game


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
players_number = int(raw_input("> "))


for i in range(players_number):
    name = raw_input("Player %s name: " % (i + 1))
    players.append(Player(name))

game = Game(players)

while game.shot <= 40:

    print "Current player %s " % game.current_player()
    x, y = user_action()
    print
    if game.fire(game.current_player(), x, y):
        print "player %s hit an enemy ship" % game.current_player()
    else:
        print "player %s didn't hit an enemy ship " % game.current_player()

    game.next_turn()

print "The winner is %s!" % game.winner()
