from flask import render_template, request, redirect, url_for
from resource_keeper import app, db
from resource_keeper.models import Category, Resource

@app.route("/")
def home():
    return render_template("categories.html")

