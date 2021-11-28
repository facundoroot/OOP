from .player import Player


class Game:
    # a property that increases everytime a gameclass is initiated
    # so we can differenciate game
    counter = 0

    def __init__(self, num_players: int, dice, target_score: int) -> None:
        self.num_players = num_players
        self.target_score = target_score
        Game.counter += 1
        self.game_num = Game.counter
        # create list of players, using the amount of player and the
        # target score for the players to win
        self.players_list_obj = [
            Player(i + 1) for i in range(self.num_players)
        ]
        # first player will be lucky
        # self.players_list_obj[0] = LuckyPlayer(1)
        self.dice = dice()

    def _game_start(self):
        print(f"{self} start")

    def _game_play(self):

        # mientras verdadero o sea siempre hasta que lo corte el return
        # voy agarrando cada player y sumandole un tiro de dado y ver si
        # supera los puntos dados en las reglas
        # si ninguno supera voy sumando a cada uno denuevo iteradamente
        while True:
            for player in self.players_list_obj:
                player.take_turn(self.dice)
                if player.has_won(self.target_score):
                    print(f"Player {player} won!")
                    return

    def _game_end(self):
        print(f"{self} is over\n")

    def play_game(self):
        self._game_start()
        self._game_play()
        self._game_end()

    def __str__(self):
        return f"Game {self.game_num} with dice {self.dice}"
