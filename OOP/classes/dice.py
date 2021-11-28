import random
from random import random as random_for_dice


class Dice:
    def roll(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class RussianRouletteDice(Dice):
    def roll(self):
        if random_for_dice() < 1 / 1000:
            return -1000
        return random.randint(1, 6)

    def __str__(self):
        return "RussianRouletteDice"


class D20Dice(Dice):
    def roll(self):
        # Standard d20 Dice
        return random.randint(1, 20)

    def __str__(self):
        return "D20Dice"


class RiggedDice(Dice):
    def __init__(self):
        self.num_run = 0

    def roll(self):
        # Every eighth run the throw is lucky.
        self.num_run += 1
        if self.num_run % 8 == 0:
            return random.randint(3, 6)
        return random.randint(1, 6)

    def __str__(self):
        return "RiggedDice"
