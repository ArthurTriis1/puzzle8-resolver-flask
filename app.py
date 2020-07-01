import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from Puzzle8Resolver import puzzle8Resolver
from Puzzle8 import Puzzle8

app = Flask(__name__)
cors = CORS(app, resource={r"/*":{"origins": "*"}})


@app.route("/")
def index():
    initialPuzzle = request.args.get("puzzle")
    puzzle = Puzzle8([int(i) for i in initialPuzzle.split(",")])
    resolve = puzzle8Resolver(puzzle)
    return jsonify(resolve)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()