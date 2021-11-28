import random


class Player:
    def __init__(self, player_id):
        # score of player
        self.score = 0
        self.player_id = player_id

    def __str__(self) -> str:

        return f"Player {self.player_id}"

    @staticmethod
    def _roll_dice():
        return random.randint(1, 6)

    def take_turn(self, dice):

        rolled_dice = dice.roll()
        self.score = self.score + rolled_dice
        print(f"Player score: {self.score} (rolled a {rolled_dice})")

        return self.score

    def has_won(self, target_score):

        player_won = False
        if self.score >= target_score:
            player_won = True

        return player_won


class LuckyPlayer(Player):
    @staticmethod
    def _roll_die():
        return random.randint(3, 6)

    def __str__(self):
        player_str = super().__str__()
        return player_str + " (lucky)"
