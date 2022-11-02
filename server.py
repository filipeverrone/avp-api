from os import environ
from waitress import serve


def serve_app(app):
    port = int(environ.get("PORT", 5000))
    app_env = environ.get("APP_ENV", 'prod')

    if app_env == 'dev':
        # Threaded option to enable multiple instances for multiple user access support
        app.run(threaded=True, port=port, host='0.0.0.0', debug=True)
    else:
        # to production
        serve(app, host="0.0.0.0", port=port)
