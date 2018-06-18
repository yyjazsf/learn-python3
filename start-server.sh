
source $(pipenv --venv)/bin/activate

export FLASK_DEBUG=1
export FLASK_APP=app.py

flask run --host=127.0.0.1 --port=3000 
