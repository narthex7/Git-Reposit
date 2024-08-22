from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)