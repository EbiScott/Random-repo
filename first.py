from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/random')
def random():
    return 'This is my first enpoint here'


if __name__ == '__main__':
    app.run(debug=True)

