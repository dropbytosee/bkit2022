from flask import Flask, request
from fibonacci import fibonacci

app = Flask(__name__)


@app.route('/')
def app_hello():
    return 'Hello, World!'


@app.route('/fibonacci')
def app_fibonacci():
    n = request.args.get('n')
    return ' '.join(map(str, fibonacci(int(n))))


if __name__ == '__main__':
    app.run()
