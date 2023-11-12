from flask import render_template, request, redirect, url_for
from resource_keeper import app, db

@app.route("/")
def home():
    return render_template("index.html")