from components import place_battleships, create_battleships, initialise_board

   
def attack(coordinates, board, ships):
    x, y = coordinates

    try:
        if board[x][y] is not None:
            ship_hit = board[x][y]
            ships[ship_hit] -= 1

            if ships[ship_hit] == 0:
                del ships[ship_hit]

            board[x][y] = None
            return True
        else:
            return False

    except IndexError as e:
        print(f"Error, list/dictionary index out of range: {e}")




def cli_coordinates_input():
    

    alphabet = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
        'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
        'Y': 25, 'Z': 26
    } #allows for chess-like coordinates

    while True:
        try:
            coords = input("Input coordinates (e.g. C4): ").upper() #input the coordinates
            if len(coords) != 2: #limits the length of the input to 2
                raise ValueError
            x, y = alphabet[coords[0]], int(coords[1])
            if x not in alphabet.values() or not (1 <= y <= 26): #limits to only 26
                raise ValueError
            return (x - 1, y - 1)
        except (ValueError, KeyError, TypeError): #in case of an error, warning issued
            print("Incorrect format. Input coordinates (e.g. C4)")


def simple_game_loop():
    print("Welcome to the Battleship Game!")

    board = initialise_board()
    ships = create_battleships()
    place_battleships(board, ships)
    
    print_board(board) #ascii format

    while any(size > 0 for size in ships.values()): # when all of the ships have size=0, it breaks the loop and ends game
        print("Your turn:")
        coordinates = cli_coordinates_input()
        shoot = attack(coordinates, board, ships)
        if shoot:
            print("You hit")
        elif shoot == False:
            print("You missed")

    print_board(board)
    print("Game over. You've sunk all battleships!")


    
def print_board(board):
    for row in board:
        print(" ".join(cell if cell is not None else "-" for cell in row))
     

if __name__ == "__main__":
    simple_game_loop()






