from stockfish import Stockfish
import os
from flask import Flask, request, jsonify
app = Flask(__name__)

mem_bytes = (os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES'))//2
print(os.cpu_count(), "CPUs", mem_bytes // (2 ** 20), "MB of memory")

stockfish = Stockfish(depth=30, parameters={
    "Debug Log File": "",
    "Contempt": 0,
    "Min Split Depth": 0,
    # More threads will make the engine stronger, but should be kept at less than the number of logical processors on your computer.
    "Threads": os.cpu_count()-1,
    "Ponder": "true",
    # Default size is 16 MB. It's recommended that you increase this value, but keep it as some power of 2. E.g., if you're fine using 2 GB of RAM, set Hash to 2048 (11th power of 2).
    "Hash": mem_bytes // (2 ** 20),
    # "MultiPV": 1,
    "Skill Level": 20,
    "Move Overhead": 10,
    # "Minimum Thinking Time": 20,
    # "Slow Mover": 100,
    # "UCI_Chess960": "false",
    # "UCI_LimitStrength": "false",
    "UCI_Elo": 9999}
)

print(stockfish.get_parameters())


@app.route('/getmove', methods=['GET'])
def respond():

    # Retrieve the name from url parameter
    fen = request.args.get("fen", None)
    maxtime = request.args.get("think_time", None)
    # For debugging
    print(request.args.keys())
    print(fen, maxtime)

    response = {}
    # # Check if user sent a fen at all
    if not fen:
        response["ERROR"] = "no fen found, please send a valid board position."
    # Check if fen is valid
    elif not stockfish.is_valid_fen(fen):
        response["ERROR"] = "invalid fen, please send a valid fen."
    else:
        stockfish.set_fen_position(fen)
        response["BESTMOVE"] = stockfish.get_best_move_time(
            maxtime if maxtime else 1000)
    # Return the response in json format
    return jsonify(response)


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support

    app.run(threaded=True, port=os.environ.port if os.environ.port else 5000)
