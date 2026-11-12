import random


def roll_dice():
    return random.randint(1,6)

def play_round(name,round_num):
    import func.vali as v
    import func.user_output as u
    round = {}
    round["round"]         = round_num
    round["player_dice"]   =  roll_dice()
    round["computer_dice"] = roll_dice()
    round["winner"]        = v.calculate_winner(round["player_dice"],round["computer_dice"],name)
    u.print_round_resoult(round["player_dice"],round["computer_dice"],round["winner"])
    return round