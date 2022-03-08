""" Python app-code """
import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


""" Set up an instance of PyMongo
    (insure Flask app is communicating with MongoDB) """
mongo = PyMongo(app)


@app.route("/")            # default url also leads to this
@app.route("/get_shoes")
def get_shoes():
    """ Retrieve all shoes for Home-page """
    shoes = mongo.db.shoes.find()
    return render_template("shoes.html", shoes=shoes)


# Run app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
