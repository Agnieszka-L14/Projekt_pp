# Napisz program zliczający punkty w grach (karcianych, planszowych itp.), realizujący:
# • definiowanie liczby oraz imion graczy,
# • definiowanie liczby punktów potrzebnych do wygranej,
# • wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy.

def define_player(player_no):
    player_points = []
    player_name = input("Podaj imię {} gracza: ".format(player_no))

    return {player_name: player_points}


def define_players():
    players = {}
    players_total = int(input("Podaj liczbę graczy od 1-8: "))
    for i in range(players_total):
        players.update(define_player(i+1))
    return players

def define_win_points():
    return int(input("Zdefiniuj ilość punktów wygranej :"))
def is_winner(players, win_points):
    for player in players.keys():
        if sum(players[player]) <= win_points:
            return True
    return False
def count_points(players,win_points):
    counter =1
    while True:
        print("\n To jest tura ", counter)
        for player in players.keys():
            player_points = int(input("Podaj punkty dla gracza {} :".format(player)))
            players[player].append(player_points)
            if is_winner(players, win_points):
                return player
        counter += 1
    return "winner"

def show_results(players, winners):
    print("\n Wygrał pracz o imieniu {}, brawo ".format(winners))
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, " -> ", points)

players = define_players()
win_points = define_win_points()
winner = count_points(players,win_points)
print(players)

show_results (players,winner)

