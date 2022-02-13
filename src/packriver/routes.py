from packriver import app
from flask import (render_template, request, redirect, url_for)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")
