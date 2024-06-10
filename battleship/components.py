import json
import random


def initialise_board(size=10): #creates a board with default size of 10x10
    board = []
    for cell in range(size):
        row = [None for cell in range(size)]
        board.append(row)
    return board


def create_battleships(filename='battleships.txt'): #creates battleships based on the txt file
    battleships = {}

    with open(filename, 'r') as f:
        for line in f:
            name, size = line.strip().split(':') #splits battleships from their size
            battleships[name] = int(size)
    return battleships


def place_battleships(board, ships, algorithm = "simple"):
    
    array = []
    for o in ships:
        array.append(o)
    
    if algorithm == "simple": #places the ships in rows by iterating them horizontally
        for i in range(len(ships)):
            for j in range(ships[array[i]]):
                board[i][j] = array[i]
        
    elif algorithm == "random": #places ships randomly
        for name, size in ships.items():
            while True:
                orientation = random.choice(["horizontal", "vertical"])
                if orientation == "horizontal":
                    x = random.randint(0, len(board[0]) - size)  #randomly chooses the coordinates
                    y = random.randint(0, len(board) - 1)
                    if all(board[y][x + i] == None for i in range(size)): # check if the coordinates are available
                        for i in range(size):
                            board[y][x + i] = name  #places the ship
                        break
                else:  # Vertical orientation
                    x = random.randint(0, len(board[0]) - 1)   #randomly chooses the coordinates
                    y = random.randint(0, len(board) - size)
                    if all(board[y + i][x] == None for i in range(size)): # check if the coordinates are available
                        for i in range(size):
                            board[y + i][x] = name   #places the ship
                        break

    elif algorithm == "custom": #places ships according to json file
        with open("placement.json", "r") as f:
            placements = json.load(f) #loads the json file

        for ship, (x, y, orientation) in placements.items():
            x, y = int(x), int(y)        #placement of ships according to json

            if orientation == "h":
                for i in range(ships[ship]): #horizontal placement of ships
                    board[y][x + i] = ship
            else:  
                for i in range(ships[ship]): #vertical placement of ships
                    board[y + i][x] = ship


                        
    return board







