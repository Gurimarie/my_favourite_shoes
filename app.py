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


@app.route("/get_shoes")    # this is actually for Gallery, not home-page!
def get_shoes():
    """ Retrieve all shoes for Home-page """
    shoes = mongo.db.shoes.find()
    return render_template("shoes.html", shoes=shoes)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")



# Run app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
