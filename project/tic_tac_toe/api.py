from flask import Flask, abort, request, jsonify

from .utilities import tic_tac_toe_winner

app = Flask(__name__)


@app.route('/winner', methods=['GET'])
def winner():
    if not request.args.get('board'):
        abort(400)
    return jsonify({'winner': None})
