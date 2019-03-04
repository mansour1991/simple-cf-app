from flask import Flask,redirect
from flask import render_template
from flask import request
import os, json
import time




app = Flask(__name__)

if os.getenv("PORT"):
    port = int(os.getenv("PORT"))
else:
    port = 8080

@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
