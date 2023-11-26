from resource_keeper import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    resources = db.relationship("Resource", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent category in the form of a string
        return "category name: {0}".format(self.category_name)


class Resource(db.Model):
    # schema for the Resource model
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(50), unique=True, nullable=False)
    resource_url = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    # text data type allows any length for field
    resource_description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent resource in the form of a string
        return "resource name: {0}".format(self.resource_name)