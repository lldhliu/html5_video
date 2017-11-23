# coding:utf-8
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def index():
    return render_template('client.html')


if __name__ == '__main__':
    app.run()
