from flask import render_template, request, redirect, url_for
from datetime import date
from resource_keeper import app, db
from resource_keeper.models import Category, Resource

@app.route("/")
def home():
    # convert cursor object returned by query into python list
    # NB each element of list represents a row of fields of model
    # row fields are accessed via dot notation
    categories = list(Category.query.all())

    # categories argument in render_template() is variable name passed to 
    # template. It is assigned to value of categories as defined above
    return render_template("categories.html", categories=categories)

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # create new row in Category table
        category = Category()
        category.category_name = request.form.get("category_name")
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("home"))
        # GET method
    return render_template("add_category.html")

@app.route("/edit_categories")
def edit_categories():
    categories = list(Category.query.all())
    return render_template("edit_categories.html", categories=categories)

@app.route("/add_resource/<category_id>", methods=["GET", "POST"])
def add_resource(category_id):
    # get row for category selected in view or 404 if not found in db
    category = Category.query.get_or_404(category_id)
    #category = Category.query.filter_by(id=category_id).first()
    # get category name from row
    category_name = category.category_name
    if request.method == "POST":
        # create new row in Resource table
        resource = Resource()
        # assign values from input form to fields in new Resource row (see models.py)
        resource.resource_name = request.form.get("resource_name")
        resource.resource_url = request.form.get("resource_url")
        resource.resource_description = request.form.get("resource_description")
        resource.category_id = category_id
        # add new record to db
        db.session.add(resource)
        db.session.commit()
        return redirect(url_for("home"))
    # if GET. Return categories to template for dropdown
    return render_template("add_resource.html", category_id=category_id, category_name = category_name)

@app.route("/view_resources/<int:category_id>", methods=["GET"])
def view_resources(category_id):
    print(category_id)
    # get rows for selected category
    #resources = Resource.query.get_or_404(category_id)
    resources = Resource.query.filter_by(category_id=category_id).all()
    return render_template("view_resources.html", resources=resources)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404