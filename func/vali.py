


def is_not_empty(input):
    if input == "":
        raise ValueError("con't be empty")

def is_int(input):
    if input.isdigit() == False:
        raise ValueError("most be a number")

def is_in_range(input,valid_range):
    if int(input) > valid_range or int(input) < 1:
        raise ValueError(f"out of range most be min 1 max {valid_range}")




def calculate_winner(player_score, computer_score,name):
    if player_score == computer_score:
        return "drow"
    if computer_score > player_score:
        return "computer"
    return name
    












