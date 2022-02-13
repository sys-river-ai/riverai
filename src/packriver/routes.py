from packriver import app
from flask import (render_template, request, redirect, url_for)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/article')
def article():
    return render_template("create-article.html")

@app.route('/create', methods=("GET", "POST"))
def create_article():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"] 
        intro = request.form["intro"] 
        return redirect(url_for("article"))