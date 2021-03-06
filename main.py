import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_time():
    return str(time.time())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)