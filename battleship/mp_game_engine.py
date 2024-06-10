from game_engine import attack, cli_coordinates_input, print_board
from components import initialise_board, create_battleships, place_battleships
import random

players = {}
ai_chosen_coords=[]
#array of already chosen coordinates by the AI so that it doesnt repeat the same move again

def generate_attack():
    while True:
        board_length =10
        x = random.randint(0, board_length-1) #random coordinates - random shooting - bad AI
        y = random.randint(0, board_length-1)
        if [x,y] not in ai_chosen_coords:
            ai_chosen_coords.append([x,y])
            break

    return (x, y)




def ai_opponent_game_loop():
    print("-------WELCOME TO MULTIPLAYER AGAINST AI BATTLESHIP------")
    print("Ctrl+C to exit")

    player_board = initialise_board()
    player_ships = create_battleships()
    place_battleships(player_board, player_ships, "custom") #can change to custom, simple or random placement



    ai_board = initialise_board()
    ai_ships = create_battleships()
    place_battleships(ai_board, ai_ships, "random") #can change to custom, simple or random placement

    

    while len(player_ships) != 0 and len(ai_ships) != 0: 
        player_coords = cli_coordinates_input() #input coordinates at your turn
        player_attack = attack(player_coords, ai_board, ai_ships)
        if player_attack:
            print("YOU HIT!")
        else:
            print("YOU MISSED")

        ai_coords = generate_attack()  #AI's turn
        ai_attack = attack(ai_coords, player_board, player_ships)
        if ai_attack:
            print("AI HIT")
        else:
            print("AI MISSED")

        print("YOUR FLEET:\n")
        print_board(player_board)
        print(" \n ")

    if len(player_ships) == 0:
        print("UNLUCKY LMAOOOOOO" if random.randint(1, 100) == 1 else "YOU LOST, TRY AGAIN!") #cheeky easter egg
    else:
        print("YOU WON, CONGRATS!")

if __name__ == "__main__":
    ai_opponent_game_loop()








