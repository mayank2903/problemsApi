from flask import Flask, jsonify, request, Response
import uuid

app = Flask(__name__)
app.debug = True

pass_result = "PASS"
fail_result = "FAIL"


@app.route('/', methods=['GET'])
def hello():
    data = 'hello'
    return jsonify({'hello': 'world'})


def evaluate_based_on_language(code, test_cases, solutions, language):
    match language:
        case "c":
            return evaluate_c_submission()
        case "cpp":
            return evaluate_cpp_submission()
        case "java":
            return evaluate_java_submission()
        case "python":
            return evaluate_py_submission()
        case default:
            pass
    return None


def evaluate_c_submission():
    return pass_result


def evaluate_cpp_submission():
    return pass_result


def evaluate_java_submission():
    return pass_result


def evaluate_py_submission():
    return pass_result


@app.route('/submissions/evaluate', methods=['POST'])
def evaluate():
    code = request.form['code']
    test_cases = request.form['test_cases']
    solutions = request.form['solutions']
    language = request.form['language']
    result = evaluate_based_on_language(code, test_cases, solutions, language)
    return jsonify({"result": result})
