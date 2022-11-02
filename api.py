from flask import Flask, request, jsonify, render_template
from json import loads
from src.formulas import main
from src.validate import validate_type_request
from src.utils import convert_to_float, take_results_positions
from src.server import serve_app

app = Flask(__name__)


@app.route('/main/', methods=['GET'])
def respond(data=None):
    if not data:
        P = request.args.get("P", None)
        R = request.args.get("R", None)
        S = request.args.get("S", None)
        n = request.args.get("n", None)
        i = request.args.get("i", None)
    else:
        i = data['i']
        n = data['n']
        P = data['P']
        R = data['R']
        S = data['S']

    response = {}

    if not n or not i:
        response['ERROR'] = 'No arguments n or i are passed!'

    response["DATA"] = main(
        i=convert_to_float(i),
        n=int(n),
        P=convert_to_float(P),
        R=convert_to_float(R),
        S=convert_to_float(S),
    )
    return jsonify(response)


@app.route('/', methods=('GET', 'POST'))
def index():
    main_result = ''
    message = ''

    if request.method == 'POST':
        i = request.form['i']
        n = request.form['n']
        triangle_key = request.form['triangle_key']
        triangle_value = request.form['triangle_value']

        print(f'i = {i}')
        print(f'n = {n}')
        print(f'triangle_key = {triangle_key}')
        print(f'triangle_value = {triangle_value}')

        data = {
            'i': i,
            'n': n,
            'P': None,
            'R': None,
            'S': None,
        }
        data[triangle_key] = triangle_value

        is_valid = validate_type_request(data)
        print(f'is_valid = {is_valid}')
        if is_valid != None:
            message = f'invalid {is_valid} field value!'
            main_result = ''
        else:
            response = respond(data)

            results = loads(response.response[0])['DATA']
            print(f'results: {results}')
            main_result = take_results_positions(results)

    return render_template(
        'home.html',
        results=main_result,
        message=message
    )


if __name__ == '__main__':
    serve_app(app)
