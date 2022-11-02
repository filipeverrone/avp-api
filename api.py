from waitress import serve
from flask import Flask, request, jsonify, render_template
from formulas import main
import os
from json import loads

app = Flask(__name__)


def convert_to_float(num):
    if not num:
        return None
    return float(num)


def take_results_positions(data: dict):
    i = data['i']
    n = data['n']
    P = data['P']
    R = data['R']
    S = data['S']

    show = ''
    for key in data.keys():
        show += f'<br>{key} = {data[key]}</br>'

    return show + '<br />'


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

        response = respond(data)

        results = loads(response.response[0])['DATA']
        print(f'results: {results}')
        main_result = take_results_positions(results)

    return render_template('home.html', results=main_result)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app_env = os.environ.get("APP_ENV", 'prod')

    if app_env == 'dev':
        # Threaded option to enable multiple instances for multiple user access support
        app.run(threaded=True, port=port, host='0.0.0.0')
    else:
        # to production
        serve(app, host="0.0.0.0", port=port)
