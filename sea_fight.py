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
#
# while shot <= 50 and taken <= 30:
#     x, y = user_action()
#     if battlefield.is_hit(x, y):
#         taken += 1
#         print "SHIPS HIT"
#     else:
#         print "SHIPS NOT HIT "
#
#     shot += 1
#
#
# if shot <= 50:
#     print "YOU HAVE LOST"
#
# if taken == 30:
#     print "YOU HAVE WON"

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
    next_player(turn)

    # 3. check if hit
    # 4. update current user's statistics (taken)


    if players[0].is_hit(x,y):
        print "player p have hit the enemy ship"
    else:
        print "player p haven't hit the enemy ship "

    turn = next_player(turn)
