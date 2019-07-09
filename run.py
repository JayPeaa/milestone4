import pymongo, os, json, bcrypt
from flask import Flask, render_template, url_for, request, session, redirect, flash
from bson.objectid import ObjectId



MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "cook-e"
RECIPE_COLLECTION = "recipes"
USER_COLLECTION = "users"
LEVEL_COLLECTION = "skill_level"
COURSE_COLLECTION = "course_type"
ALLERGENS_COLLECTION = "allergens"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo: %s") % e 
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][RECIPE_COLLECTION]
user_coll = conn[DBS_NAME][USER_COLLECTION]
level_coll = conn[DBS_NAME][LEVEL_COLLECTION]
course_coll = conn[DBS_NAME][COURSE_COLLECTION]
allergens_coll = conn[DBS_NAME][ALLERGENS_COLLECTION]

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
    recipes = coll.find()
    return render_template("recipes.html", recipes=recipes,
    level = level_coll.find(),
    course = course_coll.find(),
    allergen = allergens_coll.find())
    
@app.route("/instructions/<item_id>")
def instructions(item_id):
    recipes = coll.find_one({"_id": ObjectId(item_id)})
    return render_template("instructions.html", recipes=recipes)

@app.route("/add_recipe")
def add_recipe():
    return render_template("addrecipe.html",
    level = level_coll.find(),
    course = course_coll.find(),
    allergen = allergens_coll.find())

@app.route("/profile")
def profile():
    '''
    Display profile page if user in session
    
    '''
    
    if 'user_name' in session:  
        user = user_coll.find_one({'user_name': session['user_name']}) #Load the user
        return render_template("profile.html", user=user) #Send user data to view
    
    return render_template("login.html")
    
    
@app.route("/register", methods=['POST', 'GET'])
def register():
    '''
    Register a new user and check that user name does not already exist
    '''
    if request.method == 'POST':
        users = user_coll
        existing_user = users.find_one({'user_name': request.form['user_name']})
        print(existing_user)
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'user_name' : request.form['user_name'], 'password' : hashpass, 'first_name' : request.form['first_name'], 'last_name' : request.form['last_name'], 'email' : request.form['email']})
            session['user_name'] = request.form['user_name']
            return redirect( url_for("profile"))
        
        flash('That username already existis!', 'flashstyling')    
        return redirect( url_for("register"))
        
    return render_template('register.html')
    

@app.route("/login", methods=['POST'])
def login():
    users = user_coll
    login_user = users.find_one({'user_name' : request.form['user_name']})
    
    if login_user:
        if bcrypt.checkpw(request.form['pass'].encode('utf-8'), login_user['password']):
            session['user_name'] = request.form['user_name']
            return redirect(url_for('recipes'))
    
    flash('Invalid username/password combination', 'flashstyling')
    return render_template("login.html")
        
       
    

@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html")
    
if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug = True)