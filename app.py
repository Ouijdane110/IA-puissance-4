import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pvp')
def pvp():
    stream = os.popen('python3 puissance4_player1_vs_player2.py')
    output = stream.read()  
    return render_template('index.html')

@app.route('/pva')
def pva():
    stream = os.popen('python3 puissance4_with_alphabeta_IA.py')
    output = stream.read()  
    return render_template('index.html')

@app.route('/pvm')
def pvm():
    stream = os.popen('python3 puissance4_with_minimax_IA.py')
    output = stream.read()
    return render_template('index.html')

@app.route('/mva')
def mva():
    stream = os.popen('python3 puissance4_minimax_vs_alphabeta.py')
    output = stream.read()
    return render_template('index.html')