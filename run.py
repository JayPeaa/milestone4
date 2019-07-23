import pymongo
import os
import bcrypt
from flask import Flask, render_template, url_for, request, session, redirect
from flask import flash
from bson.objectid import ObjectId

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "cook-e"
RECIPE_COLLECTION = "recipes"
USER_COLLECTION = "users"
LEVEL_COLLECTION = "skill_level"
COURSE_COLLECTION = "course_type"
ALLERGENS_COLLECTION = "allergens"


def mongo_connect(url):
    """
    Function to connect to Mongo Database
    """
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

app = Flask(__name__)


@app.route("/about")
def about():
    """
    Route to about page
    """
    return render_template("about.html")


@app.route("/contact")
def contact():
    """
    Route to contact page
    """
    return render_template("contact.html")


@app.route("/")
@app.route("/recipes")
def recipes():
    """
    Route to recipes page, which is effectively the home page,
    returns level, course and allergen collections to view and
    makes use of the data for the filters
    """
    recipes = coll.find()
    return render_template("recipes.html", recipes=recipes,
                           level=level_coll.find(),
                           course=course_coll.find(),
                           allergen=allergens_coll.find())


@app.route("/filter", methods=["POST"])
def filter():
    """
    Filter view to view by skill level, course type of excluded
    allergens. It excludes specific allergens from the list as
    oppossed to including them.  Also returns other collection info
    to the view for filters.
    """
    recipes = coll
    filter_with = {}
    exclude_allergens = ''

    skill_level = request.form.get('skill_level')
    if skill_level is not None:
        filter_with['skill_level'] = skill_level

    course_type = request.form.get('course_type')
    if course_type is not None:
        filter_with['course_type'] = course_type

    exclude_allergens = request.form.getlist('allergens')
    if exclude_allergens is None:
        exclude_allergens = []

    my_recipes = recipes.find({'$and': [filter_with,
                              {'allergens': {'$nin': exclude_allergens}}]})

    return render_template("recipes.html", recipes=my_recipes,
                           level=level_coll.find(), course=course_coll.find(),
                           allergen=allergens_coll.find())


@app.route('/search', methods=["GET", "POST"])
def search():
    """
    Search view for search bar. Gets search term from view and
    utilises a text index on Recipes collection, recipe_name field.
    """
    recipes = coll
    search_word = request.form.get('search')
    search_results = recipes.find({'$text': {'$search': search_word}})
    return render_template('recipes.html', recipes=search_results,
                           search_word=search_word,
                           level=level_coll.find(),
                           course=course_coll.find(),
                           allergen=allergens_coll.find())


@app.route("/instructions/<item_id>")
def instructions(item_id):
    """
    This route lists the individual recipes using dynamic referencing
    with the item_id being unique.
    """
    recipes = coll.find_one({"_id": ObjectId(item_id)})
    return render_template("instructions.html", recipes=recipes)


@app.route("/add_recipe")
def add_recipe():
    """
    Add recipe route returns collections to view for filters and
    renders the add recipe from.
    """
    level = level_coll.find()
    course = course_coll.find()
    allergen = allergens_coll.find()

    return render_template("addrecipe.html", level=level,
                           course=course, allergen=allergen)


@app.route("/insert_recipe", methods=['GET', 'POST'])
def insert_recipe():
    """
    After the addrecipe.html has been submited this route is called
    to insert the recipe to the database.
    """
    recipes = coll
    form = {'recipe_name': request.form['recipe_name'],
            'description': request.form['description'],
            'allergens': request.form.getlist('allergens'),
            'course_type': request.form['course_type'],
            'cuisine': request.form['cuisine'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions'],
            'serves': request.form['serves'],
            'skill_level': request.form['skill_level'],
            'time_required': request.form['time_required'],
            'user_name': request.form['user_name'],
            'recipe_image': request.form['recipe_image']}
    recipes.insert_one(form)
    flash('Your New Recipe Has Been Added Below')
    return redirect("recipes")


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    """
    This route renders the edit recipe form. Various collections are returned
    to the view for the filters/select fields to utilise
    """
    recipes = coll.find_one({"_id": ObjectId(recipe_id)})
    user = user_coll.find()
    level = level_coll.find()
    course = course_coll.find()
    allergen = allergens_coll.find()
    return render_template("editrecipe.html", recipes=recipes,
                           user=user, level=level, course=course,
                           allergen=allergen)


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    """
    This (dynamic) route is for updating changes to the database and is
    only available to authors of the recipes.  i.e. where the session
    user is equal to the recipe author.  Get is used to retrive the
    info and $set is used to amend only the fields which have been
    edit as to not change the database structure.
    """
    recipes = coll
    recipes.update({'_id': ObjectId(recipe_id)},
                   {"$set": {
                    "recipe_name": request.form.get("recipe_name"),
                    "cuisine": request.form.get("cuisine"),
                    "description": request.form.get("description"),
                    "course_type": request.form.get("course_type"),
                    "time_required": request.form.get("time_required"),
                    "skill_level": request.form.get("skill_level"),
                    "ingredients": request.form.get("ingredients"),
                    "allergens": request.form.getlist("allergens"),
                    "serves": request.form.get("serves"),
                    "instructions": request.form.get("instructions")
                    }})
    flash('Your Changes Have Been Saved')
    return redirect(url_for('recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """
    Another dynamic route utilised for deleting recipes.  Only
    available to recipe authors.
    """
    coll.remove({'_id': ObjectId(recipe_id)})
    flash('Recipe Deleted')
    return redirect(url_for('recipes'))


@app.route('/likes/<item_id>')
def likes(item_id):
    """
    Another dynamic route utilised for liking recipes.  Allows
    users to see popularity of recipes.
    """
    coll.find_one_and_update(
        {'_id': ObjectId(item_id)},
        {'$inc': {'likes': 1}})
    return redirect(url_for('instructions', item_id=item_id))


@app.route("/profile")
def profile():
    '''
    Display profile page if user in session

    '''

    if 'user_name' in session:
        user = user_coll.find_one({'user_name': session['user_name']})
        users_recipes = coll.find({'user_name': session['user_name']})
        return render_template("profile.html", user=user,
                               users_recipes=users_recipes)

    return render_template("login.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    '''
    Register a new user and check that user name does not already exist
    Also utilise bcrypt for added security.
    '''
    if request.method == 'POST':
        users = user_coll
        existing_user = users.find_one,
        ({'user_name': request.form['user_name']})
        print(existing_user)

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                                     bcrypt.gensalt())
            users.insert({'user_name': request.form['user_name'],
                          'password': hashpass,
                          'first_name': request.form['first_name'],
                          'last_name': request.form['last_name'],
                          'email': request.form['email']})
            session['user_name'] = request.form['user_name']
            session['logged_in'] = True
            return redirect(url_for("profile"))

        flash('That username already existis!', 'flashstyling')
        return redirect(url_for("register"))

    return render_template('register.html')


@app.route("/login", methods=['POST'])
def login():
    """
    User login route
    """
    users = user_coll
    login_user = users.find_one({'user_name': request.form['user_name']})

    if login_user:
        if bcrypt.checkpw(request.form['pass'].encode('utf-8'),
                          login_user['password']):
            session['user_name'] = request.form['user_name']
            session['logged_in'] = True
            return redirect(url_for('recipes'))

    flash('Invalid username/password combination', 'flashstyling')
    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    User log out route
    """
    session.clear()
    return render_template("login.html")


if __name__ == "__main__":
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
