import func.user_output as u

import func.gameplay as gp
import json_f.main_json as j









def main():
    while True:
        chooce = u.start_menu_chooce()
        if chooce == 1:
            game = gp.create_new_game()
            resolt_game = gp.start_game(game)
            u.print_game_resoult(resolt_game)
            j.save_game(resolt_game)
        if chooce == 2:
            history = j.load_game_history()
            if len(history) == 0:
                print("no games yet")
                continue    
            u.print_games_history(history)
        if chooce == 3:
            if len(j.load_game_history()) == 0:
                    print("no games yet")
                    continue
            u.print_statistics()
        if chooce == 4:
            exit()

        



if __name__ == "__main__":
    main()