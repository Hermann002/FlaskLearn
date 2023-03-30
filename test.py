from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def test():
    global identifiant
    identifiant = str(random.randint(0, 100))
    form = f'digiplus{identifiant}'
    return identifiant

@app.route('/live')
def live():
    return f'votre identifiant est {identifiant}'