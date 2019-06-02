import pymongo
import os
from flask import Flask, render_template, url_for, request, session, redirect
import bcrypt


MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "cook-e"
COLLECTION_NAME = "recipes"
USER_COLLECTION = "users"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo: %s") % e 
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]
user_coll = conn[DBS_NAME][USER_COLLECTION]

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
    if 'user_name' in session:
        return 'You are logged in as ' + session['user_name']
    
    return render_template("profile.html")
    
@app.route("/register", methods=['POST', 'GET'])
def register():
        
    if request.method == 'POST':
        users = user_coll
        existing_user = users.find_one({'user_name': request.form['user_name']})
        print(existing_user)
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'user_name' : request.form['user_name'], 'password' : hashpass, 'first_name' : request.form['first_name'], 'last_name' : request.form['last_name'], 'email' : request.form['email']})
            session['user_name'] = request.form['user_name']
            return redirect( url_for("profile"))
            
        return 'That username already existis!'
        
    return render_template('register.html')
    
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return render_template("profile.html")
    
if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug = True)