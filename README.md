# Economic Engineering API

## Test locally

1. run the scripts below:

```
python3 -m venv venv/
source venv/bin/activate
pip3 install -r requirements.txt
```

2. create a .env file with the keys below:

```
PORT=4000
APP_ENV=dev
```

3. run the script below, and access localhost/$PORT:

```
python3 api.py
```

4. at end, deactivate your virtual env:

```
deactivate
```

## Access heroku hosted website

[Website](https://fit-avp-api.herokuapp.com)
