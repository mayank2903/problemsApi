from flask import Flask, jsonify, request, Response
import uuid

app = Flask(__name__)
app.debug = True

problems = {
    '1': {
        'id': '1',
        'statement': 'problem statement contents',
        'test_cases': ['test case1', 'testcase2'],
        'solutions': ['solution1', 'solution2'],
    },
    '2': {
        'id': '2',
        'statement': 'problem statement contents',
        'test_cases': ['test case1', 'testcase2'],
        'solutions': ['solution1', 'solution2'],
    },
    '3': {
        'id': '3',
        'statement': 'problem statement contents',
        'test_cases': ['test case1', 'testcase2'],
        'solutions': ['solution1', 'solution2'],
    }
}


@app.route('/', methods=['GET'])
def hello():
    data = 'hello'
    return jsonify({'data': data})


@app.route('/problems/<string:problem_id>', methods=['GET'])
def get_method(problem_id):
    # todo: optimize below for faster lookup.
    if problem_id in problems.keys():
        return jsonify(problems[problem_id])
    else:
        return {}


@app.route('/problems/', methods=['GET'])
def list_method():
    return jsonify(problems)


@app.route('/problems', methods=['POST'])
def insert_method():
    statement = request.form['statement']
    test_cases = request.form['test_cases']
    solutions = request.form['solutions']
    id = str(uuid.uuid4())
    problems[id] = {
        'id': id,
        'statement': statement,
        'test_cases': test_cases,
        'solutions': solutions
    }
    return jsonify(problems[id])


@app.route('/problems/<string:problem_id>', methods=['PATCH'])
def patch_method(problem_id):
    if problem_id not in problems.keys():
        # throw 404 or something
        return {}

    updated_problem = problems[problem_id]
    if 'statement' in request.form.keys():
        updated_problem['statement'] = request.form['statement']
    if 'test_cases' in request.form.keys():
        updated_problem['test_cases'] = request.form['test_cases']
    if 'solutions' in request.form.keys():
        updated_problem['solutions'] = request.form['solutions']

    problems[problem_id]=updated_problem
    return jsonify(updated_problem)


@app.route('/problems/<string:problem_id>', methods=['DELETE'])
def delete_method(problem_id):
    del problems[problem_id]
    return Response(status=204)

