import func.vali as v
import json_f.main_json as j



def start_menu_chooce():
    while True:
        print(f"================================")
        print(f"          ROLL DICE")
        print(f"================================")
        print(f"1. Start New Game")
        print(f"2. View Game History")
        print(f"3. View Statistics")
        print(f"4. Exit")
        try:
            chooice = input("please enter your chooice ")
            v.is_not_empty(chooice)
            v.is_int(chooice)
            v.is_in_range(chooice,4)
            return int(chooice)
        except ValueError as e:
            print("Error:", e)



def chooce_name():
    while True:
        try:
            name = input("please enter your name ")
            v.is_not_empty(name)
            return name
        except ValueError as e:
            print("Error:",e)


def chooce_rounds():
    while True:
        try:
            rounds = input("how many rounds you want to play ")
            v.is_not_empty(rounds)
            v.is_int(rounds)
            v.is_in_range(rounds,10)
            return int(rounds)
        except ValueError as e:
            print("Error", e)

def print_round_resoult(p_points,c_points,winner):
    print(f"your:     🎲 {p_points}")
    print(f"computer: 🎲 {c_points}")
    if winner == "drow":
        print("this round ends whith drow ")
    else:
        print(f"{winner} wins this round!")


def print_game_resoult(game):
    print(f"================================")
    print(f"        GAME OVER")
    print(f"================================")
    print(f"{game["player_name"]}: {game["player_score"]} points")
    print(f"computer: {game["computer_score"]} points")
    print(f"WINNER: {game["winner"]}")

def print_games_history(games):
    for game in games:
        print(f"player name: {game["player_name"]} rounds: {game["rounds"]} player_score: {game["player_score"]} computer_score: {game["computer_score"]} winner: {game["winner"]}")

def print_statistics():
    name = chooce_name()
    if j.player_games(name) > 0:
        games = j.player_games(name)
        player_wins = j.count_winns(name,name)
        computer_wins = j.count_winns("computer",name)
        drow = j.count_winns("drow",name)
        present = player_wins*100/games
        print(f"games: {games} player winns {player_wins} computer winns {computer_wins} drows {drow} The player's success rates {present}"  )
    else:
        print(f"player {name} is not exsists")
