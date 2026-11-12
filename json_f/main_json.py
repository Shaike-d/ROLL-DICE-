from pathlib import Path
import json


PATH = Path(__file__).parent / "game_history.json"

def load_game_history():
    with open(PATH, 'r') as file:
        games = json.load(file)
        return games


def save_game(game:dict):
    games = load_game_history()
    games.append(game)
    with open(PATH, 'w') as file:
        json.dump(games,file,indent=4)


def count_winns(by_how,name):
    counter = 0
    games = load_game_history()
    for game in games:
        if game["player_name"] == name:
            if game["winner"] == by_how:
                counter += 1
    return counter


def player_games(name):
    games = load_game_history()
    counter = 0
    for game in games:
        if game["player_name"] == name:
           counter += 1
    return counter


    