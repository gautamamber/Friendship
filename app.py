from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/qa')
def qa():
    return render_template('qa.html')
@app.route('/facts')
def facts():
    return render_template('facts.html')
@app.route('/aboutf')
def aboutf():
    return render_template('aboutf.html')
@app.route('/meter')
def meter():
    return render_template('meter.html')
if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)