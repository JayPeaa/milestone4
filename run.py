import pymongo
import os
from flask import Flask, render_template

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "cook-e"
COLLECTION_NAME = "recipes"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo: %s") % e 
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    
@app.route("/recipes")
def recipes():
    return render_template("recipes.html")
    
@app.route("/profile")
def profile():
    return render_template("profile.html")


    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug = True)