# PyChess

python3 -m venv packages

source packages/bin/activate

pip3 freeze > requirements.txt

pip3 uninstall -r requirements.txt -y


## Setup
sudo apt install stockfish python3 python3-pip python3-venv

pip3 install -r requirements.txt

flask --app server.py --debug run
