from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/produto1')
def produto1():
    return render_template('produto1.html')

@app.route('/produto2')
def produto2():
    return render_template('produto2.html')