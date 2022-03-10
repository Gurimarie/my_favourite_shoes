""" Python app-code """
import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


""" Set up an instance of PyMongo
    (insure Flask app is communicating with MongoDB) """
mongo = PyMongo(app)


@app.route("/")             # default url also leads to this
@app.route("/home_page")
def home_page():
    return render_template("index.html")


@app.route("/get_shoes")    # MUST ADD "ONLY PUBLIC!"
def get_shoes():
    """ Retrieve all shoes for Gallery-page """
    shoes = list(mongo.db.shoes.find())
    return render_template("shoes.html", shoes=shoes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("This username already exists! Please try again.")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        # Put the new user into a "session"-cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful! You may now upload and share your own favourite shoes!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check if entered password matches hashed password in db
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))

            else:
                # If password doesn't match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # If username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the session-user's username from db (and only username)
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    shoes = list(mongo.db.shoes.find())

    if session["user"]:
        return render_template("profile.html", shoes=shoes, username=username)

    # If session-cookie is gone, redirect to login (for security) 
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove the users session-cookie to log out
    flash("You have been logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_shoes", methods=["GET", "POST"])
def add_shoes():
    if request.method == "POST":
        is_private = "yes" if request.form.get("is_private") else "no"
        shoes = {
            "category_name": request.form.get("category_name"),
            "shoes_name": request.form.get("shoes_name"),
            "shoes_description": request.form.get("shoes_description"),
            "brand_name": request.form.get("brand_name"),
            "comfort_level": request.form.get("comfort-level"),
            "design_level": request.form.get("design-level"),
            "construction_level": request.form.get("construction-level"),
            "heel_height": request.form.get("heel_height"),
            "toe_shape": request.form.get("toe_shape"),
            "shoes_image": request.form.get("shoes_image"),
            "username": session["user"],
            "date_added": request.form.get("date_added"),
            "is_private": is_private
        }
        mongo.db.shoes.insert_one(shoes)
        flash("New shoes successfully added!")
        return redirect(url_for("get_shoes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_shoes.html", categories=categories)


@app.route("/edit_shoes/<shoes_id>", methods=["GET", "POST"])
def edit_shoes(shoes_id):
    if request.method == "POST":
        is_private = "yes" if request.form.get("is_private") else "no"
        submit = {
            "category_name": request.form.get("category_name"),
            "shoes_name": request.form.get("shoes_name"),
            "shoes_description": request.form.get("shoes_description"),
            "brand_name": request.form.get("brand_name"),
            "comfort_level": request.form.get("comfort-level"),
            "design_level": request.form.get("design-level"),
            "construction_level": request.form.get("construction-level"),
            "heel_height": request.form.get("heel_height"),
            "toe_shape": request.form.get("toe_shape"),
            "shoes_image": request.form.get("shoes_image"),
            "username": session["user"],
            "date_added": request.form.get("date_added"),
            "is_private": is_private
        }
        mongo.db.shoes.update_one({"_id": ObjectId(shoes_id)}, {"$set": submit})
        flash("Record successfully updated.")
        return redirect(url_for('profile', username=session['user']))

    shoes = mongo.db.shoes.find_one({"_id": ObjectId(shoes_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_shoes.html", shoes=shoes, categories=categories)


@app.route("/delete_shoes/<shoes_id>")
def delete_shoes(shoes_id):
    mongo.db.shoes.delete_one({"_id": ObjectId(shoes_id)})
    flash("This record has now been deleted")
    return redirect(url_for('profile', username=session['user']))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Run app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
