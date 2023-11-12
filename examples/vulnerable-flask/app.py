from flask import Flask
import os
app = Flask(__name__)

@app.route('/login/<name>')
def login(name):
    os.system(name)
    return 'finished'

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
