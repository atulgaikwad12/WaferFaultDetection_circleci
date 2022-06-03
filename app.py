# This file is replaced by main.py file. So ignore this one. 
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Flask app is running"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)


