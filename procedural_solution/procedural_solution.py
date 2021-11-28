import random


def player_move(i, previous_score):
    player_roll = random.randint(1, 6)
    player_score = previous_score + player_roll
    # le sumo 1 porque i es el numero de player, y como son indices vienen 0 y 1 
    # y necesitamos 1 y 2
    print(f"Player {i+1} score: {player_score} (rolled a {player_roll})")
    return player_score


player_scores = [0, 0]
finished = False

# hago loop para los dos jugadores, el primero que suma mas de 100 termina el loop
# se va a repetir este loop para los dos jugadores hasta que en algun momento uno pase 100
while not finished:
    # con enumerta no solo recorre la lista sino que crea un indice para cada elemento de la lista
    # en este caso seria player_scores[0] = 0 y player_scores[1] = 0
    for player_number, player_score in enumerate(player_scores):
        player_scores[player_number] = player_move(player_number, player_score)
        if player_scores[player_number] >= 100:
            print(f"Player {player_number+1} wins!")
            finished = True
            break
