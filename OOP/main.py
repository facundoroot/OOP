from classes.game import Game
from classes.dice import RussianRouletteDice, D20Dice, RiggedDice


if __name__ == '__main__':
    game1 = Game(num_players=2, dice=RussianRouletteDice, target_score=20)
    game2 = Game(num_players=3, dice=D20Dice, target_score=50)
    game3 = Game(num_players=4, dice=RiggedDice, target_score=40)

    game2.play_game()
    game3.play_game()
    game1.play_game()
