





def create_new_game():
    import func.user_output as u
    game = {}
    game["player_name"]    = u.chooce_name()
    game["rounds"]         = u.chooce_rounds()
    game["player_score"]   = 0
    game["computer_score"] = 0
    game["winner"]         = None
    game["results"]        = []
    return game

def add_round(game:dict,round:dict):
    print(round)
    game["results"].append(round)
    update_results(game,round)


def update_game_winner(game):
    if game["player_score"] > game["computer_score"]:
        game["winner"] = game["player_name"]
    elif game["computer_score"] > game["player_score"]:
            game["winner"] = "computer"
    elif game["computer_score"] == game["player_score"]:
         game["winner"] = "drow"


def update_results(game,round):
    if round["winner"] == game["player_name"]:
        game["player_score"] += 1
    if round["winner"] == "computer":
        game["computer_score"] += 1
    update_game_winner(game)
    
       
    

def start_game(game:dict):
    import func.round as r
    round_num = 0
    while True:
        round_num += 1
        if round_num <= game["rounds"]:
            result_round = r.play_round(game["player_name"],round_num)
            add_round(game,result_round)#dict,dict
        else:
            break
    return game
