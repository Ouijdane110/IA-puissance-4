import os
from flask import Flask
app = Flask(__name__)

html = """<div style='background-image: url("https://img.youtube.com/vi/0lf5Htn4zEE/sddefault.jpg"); background-size: cover; background-repeat: no-repeat; background-position: center; width: 100%; height: 100vh; display : flex; justify-content : center; align-items : center'>
            <a href='/pvp'>
                <button style='background : red; padding: 15px; font-size : 15px; margin : 0 20px; cursor : pointer; border : none; box-shadow: 10px 10px 18px -9px rgba(0,0,0,0.75);'>Player 1 vs Player 2</button>
            </a>
            <a href='/pva'>
                <button style='background : yellow; padding: 15px; font-size : 15px; margin : 0 20px; cursor : pointer; border : none; box-shadow: 10px 10px 18px -9px rgba(0,0,0,0.75);'>Player 1 vs Alpha Beta</button>
            </a>
            <a href='/pvm'>
                <button style='background : red; padding: 15px; font-size : 15px; margin : 0 20px; cursor : pointer; border : none; box-shadow: 10px 10px 18px -9px rgba(0,0,0,0.75);'>Player 1 vs Minimax</button>
            </a>
            <a href='/mva'>
                <button style='background : yellow; padding: 15px; font-size : 15px; margin : 0 20px; cursor : pointer; border : none; box-shadow: 10px 10px 18px -9px rgba(0,0,0,0.75);'>Minimax vs Alpha Beta</button>
            </a>
        </div>"""

@app.route('/')
def home():
    return html

@app.route('/pvp')
def pvp():
    stream = os.popen('python3 puissance4_player1_vs_player2.py')
    output = stream.read()  
    return html

@app.route('/pva')
def pva():
    stream = os.popen('python3 puissance4_with_alphabeta_IA.py')
    output = stream.read()  
    return html

@app.route('/pvm')
def pvm():
    stream = os.popen('python3 puissance4_with_minimax_IA.py')
    output = stream.read()
    return html

@app.route('/mva')
def mva():
    stream = os.popen('python3 puissance4_minimax_vs_alphabeta.py')
    output = stream.read()
    return html