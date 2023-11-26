# Flask "Resource Keeper" App
#############################
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
        return redirect(url_for("view_resources", category_id = category_id))
    # if GET. Return categories to template for dropdown
    return render_template("add_resource.html", category_id=category_id, category_name = category_name)

@app.route("/view_resources/<int:category_id>", methods=["GET"])
def view_resources(category_id):
    # get relevant category_name to show at head of list
    category = Category.query.get_or_404(category_id).category_name
    # get rows for selected category
    resources = Resource.query.filter_by(category_id=category_id).all()
    return render_template("view_resources.html", resources=resources, category = category)


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method=="POST":
        category.category_name=request.form.get("category_name")
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>", methods=["GET"]) # id passed in url
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("home"))


# 404 error handler for non-existant url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 500 sql errors handler
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


@app.route("/delete_resource/<int:resource_id>", methods=["GET"]) # id passed in url
def delete_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    category_id = resource.category_id
    db.session.delete(resource)
    db.session.commit()
    return redirect(url_for("view_resources", category_id = category_id))


@app.route("/edit_resource/<int:resource_id>", methods=["GET","POST"]) # id passed in url
def edit_resource(resource_id):
    # get row for current resource using resource_id passed in GET
    resource = Resource.query.get_or_404(resource_id)
    # get category id from row returned above
    category_id = resource.category_id
    # get all categories to pass to select dropdown in edit form view
    categories = list(Category.query.all())
    # get current_category value to use in select dropdown
    current_category = (Category.query.get_or_404(category_id)).category_name
    if request.method=="POST":
        # update database with input from form
        resource.category_name=request.form.get("category_name")
        # The resource.url is not got from form in edit view (as below) so db value is unchanged
        #resource.resource_url = request.form.get("resource_url")
        resource.resource_description = request.form.get("resource_description")
        resource.resource_name = request.form.get("resource_name")
        resource.category_id = request.form.get("category_id")
        db.session.add(resource)
        db.session.commit()
        # redirect user to resources view for original category
        return redirect(url_for("view_resources", category_id = category_id))
    return render_template("edit_resource.html", 
        resource = resource, categories = categories, category_id = category_id, current_category = current_category)