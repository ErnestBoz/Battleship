
from flask import Flask, render_template, request, jsonify, json
from game_engine import attack
from mp_game_engine import generate_attack
from components import create_battleships, place_battleships, initialise_board
app = Flask(__name__)

player_board = initialise_board()
player_ships = create_battleships()
player_chosen_coords = [] #prevents shooting same cell twice
ai_board = initialise_board()
ai_ships = create_battleships()
place_battleships(ai_board, ai_ships, "random")

@app.route("/", methods=['GET'])
def root():
    return render_template("main.html", player_board=player_board)

@app.route("/placement", methods=['GET', 'POST'])
def placement_interface():
    if request.method == 'POST':
        json.dump(request.get_json(), open("placement.json", mode="w")) 
        place_battleships(player_board, player_ships, "custom") #allows to place battleships
        return jsonify({'message': 'Received'}), 200
    elif request.method == 'GET':
        return render_template("placement.html", ships=player_ships, board_size=len(player_board)) #returns the battleships back to root

@app.route("/attack", methods=['GET'])
def process_attack():# generate_attack() function but tweaked
    
    while True:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        player_coords = (x,y)
        if [x,y] in player_chosen_coords:
            raise() 
        else:
            player_chosen_coords.append([x,y]) #doesn't allow to shoot the same cell again by putting the coordinates into the empty array
            break

    player_shoot = attack(player_coords, ai_board, ai_ships)
    ai_shoot = generate_attack()
    attack(ai_shoot, player_board, player_ships)

    game_over_message = "Game Over {} wins"
    if not player_ships:
        return jsonify({'hit': player_shoot, 'AI_Turn': ai_shoot, 'finished': game_over_message.format("AI")}) #message when player wins
    elif not ai_ships:
        return jsonify({'hit': player_shoot, 'AI_Turn': ai_shoot, 'finished': game_over_message.format("Player")}) #message when AI wins
    return jsonify({'hit': player_shoot, 'AI_Turn': ai_shoot})
    

if __name__ == "__main__":
    app.run()