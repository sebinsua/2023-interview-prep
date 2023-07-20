import random

def solution(seed, n):
    class Die(object):
        def __init__(self, seed, n):
            self.seed = seed
            self.n = n

        def __get__(self, instance, owner):
            random.seed(self.seed)
            return int(random.random() * self.n + 1)

    class Game(object):
        die = Die(seed, n)

    return Game.die
