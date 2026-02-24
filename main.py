import random
from flask import Flask, render_template

app = Flask(__name__)

app.run(debug=True)
@app.route('/coinFlip')
def coinFlip():
    return render_template('index.html')
@app.route('/coinData')
def coinData():
    rnd = random.randint(0,1)
    return ["TAILS", "HEADS"][rnd]
