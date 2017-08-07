from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('aboutf.html')
if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)