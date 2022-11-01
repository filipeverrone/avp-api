from flask import Flask, request, jsonify
from formulas import main

app = Flask(__name__)


def convert_to_float(num):
    if not num:
        return None
    return float(num)


@app.route('/main/', methods=['GET'])
def respond():
    P = request.args.get("P", None)
    R = request.args.get("R", None)
    S = request.args.get("S", None)
    n = request.args.get("n", None)
    i = request.args.get("i", None)

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


@app.route('/')
def index():
    return '''
        <div>
            <h1>Economic Engineering</h1>
            <h2>Use /main/ passing values of n, i and P, R or S</h2>
            <h3>To convert i, use /convert</h3>
            <p>
                Obs.: The i value must be in percent (for example, 25 if your i is 25%)
            </p>
        </div>
    '''


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)

    # to production
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
