import os
import sys
import json
import argparse
from flask import (
    Flask, render_template, request, jsonify, redirect
)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
    static_url_path='/static',
    static_folder='static',
    template_folder='templates',
)

@app.route('/nevergonnagiveyouup')
def index():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)

@app.route('/nevergonnagiveyouup/home')
def home():
    num_str = "21"
    return render_template("home.html",num_str=num_str)

@app.route('/nevergonnagiveyouup/hello')
def hello():
    return jsonify({'message': "hello"})

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=5000)
    parser.add_argument('-d', '--debug',action='store_true')
    args = parser.parse_args()
    app.run(host="0.0.0.0",port=args.port,debug=args.debug)
