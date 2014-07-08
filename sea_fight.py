from model import Player


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

def next_player(current_player):
    return (current_player + 1) % players_number


# My game

print "How many players ?"
players_number = int(raw_input("> "))

for i in range(players_number):
    name = raw_input("Player %s name: " % (i + 1))
    players.append(Player(name))

turn = 0
shot = 0

for i in range(2):                              # TODO: change this behaviour
    print "it's {}'s turn".format(players[i])

    # game logic

    # 1. get user's action
    x,y  = user_action()
    # 2. get next user battlefield
    print "your enemy is %s " % players[next_player(turn)]
    # 3. check if hit
    if players[next_player(turn)].battlefield.is_hit(x,y):
        print "player %s  hit an enemy ship" % players[turn]
    # 4. update current user's statistics (taken)
        players[turn].hit += 1
    else:
        print "player %s didn't hit an enemy ship " % players[turn]

    turn = next_player(turn)
