from flask import Flask, render_template, request, jsonify
from nqueen_solver import solve_n_queen
from nknight_tour import solve_knight_tour

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    n = int(data['n'])
    problem = data['problem']

    if problem == 'queen':
        steps = solve_n_queen(n)
    elif problem == 'knight_tour':
        steps = solve_knight_tour(n)
    else:
        return jsonify(error="Unknown problem type"), 400

    if not steps:
        return jsonify(steps=[])  # Return empty if no solution

    return jsonify(steps=steps)

if __name__ == '__main__':
    app.run(debug=True)
