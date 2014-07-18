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

            if self.field[x][y]== 0:
                self.field[x][y] = 1
                self.ships += 1

    def is_hit(self, x, y):
        return self.field[x][y]



class Player(object):

    def __init__(self,name='computer'):

        self.name = name
        self.battlefield = Battlefield()
        self.hit = 0

    def __str__(self):
        return self.name


class Game(object):

    def __init__(self, players):
        self.players = players
        self.shot = 0
        self.turn = 0
        self.round = 0  # current player
        self.hit = 0   # hit ship

    def next_player(self):
        return (self.round + 1) % len(self.players)

    def current_player(self):           #define current player
        return self.players[self.round]

    def fire(self, player, x, y):
        enemy = self.players[self.next_player()]
        take = enemy.battlefield.is_hit(x,y)
        if take and enemy.battlefield.field[x][y] != 2:
            player.hit += 1
            enemy.battlefield.field[x][y] = 2

        return take

    def next_turn(self):
        self.round = (self.round + 1) % len(self.players)
        self.shot += 1

        if self.round == 0:
            self.turn += 1


    def winner(self):
        best_hit = 0

        for player in self.players:
            # get player with max 'hit'
            if player.hit > best_hit:
                max = player
        return max
