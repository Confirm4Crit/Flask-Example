from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is {}</p>'.format(user_agent)
#
#
# @app.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400
#
#
# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response
