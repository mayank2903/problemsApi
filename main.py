from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    data = 'hello'
    return jsonify({'data': data})


@app.route('/problems/<int:problem_id>', methods=['GET'])
def get_method(problem_id):
    return jsonify({
        'id': problem_id,
        'statement': 'problem statement contents',
        'test_cases': ['test case1', 'testcase2'],
        'solutions': ['solution1', 'solution2'],
    })


@app.route('/problems/', methods=['GET'])
def list_method():
    return jsonify([{
        'id': '1',
        'statement': 'problem statement contents',
        'test_cases': ['test case1', 'testcase2'],
        'solutions': ['solution1', 'solution2'],
    },
        {
            'id': '2',
            'statement': 'problem statement contents',
            'test_cases': ['test case1', 'testcase2'],
            'solutions': ['solution1', 'solution2'],
        },
        {
            'id': '3',
            'statement': 'problem statement contents',
            'test_cases': ['test case1', 'testcase2'],
            'solutions': ['solution1', 'solution2'],
        }])


@app.route('/problems', methods=['POST'])
def insert_method():
    statement = request.form['statement']
    test_cases = request.form['test_cases']
    solutions = request.form['solutions']
    return jsonify({
        'id': '1',
        'statement': statement,
        'test_cases': test_cases,
        'solutions': solutions,
    })


@app.route('/problems/<int:problem_id>', methods=['PATCH'])
def patch_method(problem_id):
    statement = request.form['statement']
    test_cases = request.form['test_cases']
    solutions = request.form['solutions']

    return jsonify({
        'id': problem_id,
        'statement': statement,
        'test_cases': test_cases,
        'solutions': solutions,
    })


@app.route('/problems/<int:problem_id>', methods=['DELETE'])
def delete_method(problem_id):
    return jsonify()
