__author__ = 'alessandro'

from .battlefield import Battlefield


class Player(object):

    def __init__(self, name='computer'):

        self.name = name
        self.battlefield = Battlefield()
        self.hit = 0

    def __str__(self):
        return self.name
