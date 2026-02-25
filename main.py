import random
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('layout.html')
@app.route('/coinFlip')
def coinFlip():
    return render_template('index.html')
@app.route('/coinData')
def coinData():
    print(request.args["vrednost"])
    rnd = random.randint(0,1)
    if rnd == 1:
        status = "HEADS"
        img_url = "https://i.postimg.cc/CBNJNfDJ/heads.png" 
    else:
        status = "TAILS"
        img_url = "https://i.postimg.cc/zysdXN8w/tails.png"
    status=["TAILS", "HEADS"][rnd]
    return {"img":img_url, "status": status}
if __name__ == '__main__':
    app.run(debug=True)
 