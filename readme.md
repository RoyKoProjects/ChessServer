# PyChess

python3 -m venv packages

source packages/bin/activate

pip freeze > requirements.txt

pip uninstall -r requirements.txt -y


## Setup

pip install -r requirements.txt

flask --app server.py --debug run