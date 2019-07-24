# Milestone Project 4

#### Data Centric Development

#### Design and Build an Interactive Cooking App

---

### App Name: Cook-e

##### See here for [Deployed App](https://cook-e.herokuapp.com/)

Cook-e is an interactive cooking app which allows users to share recipes online. It enables users to browse recipes uploaded by other users as well as add, edit and delete their own recipes. This app is built using Flask and MongoDB, a NoSQL or document store database but incorporates a number or other technologies.

Having recipes stored online in a system which allows users to filter and quickly reference their own personal recipes at the click of a button is infinitely faster than using traditional cookbooks. In addition, with the advent of tablets and virtual assistants such as google home, more and more users are making use of digital media when preparing meals in the home.


## UX

The UX has been designed with the end user in mind and as expectations in terms of front-end design are ever increasing, I opted to utilise Materialize.css for my design and responsive layout. Materialize.css is a library of UI components designed by Google with the aim of providing a unified and consistent user experience.

#### User Stories

- As the app developer I want to build an app which allowed users to share recipes in one convenient location.
- As the app developer I want these recipes to be presented in a user friendly and secure way which allows users to only edit or delete their own recipes.
- As the app developer I want to create an app which was very visual with quirky animation and a move away from a traditional text-based navigation menu.
- As a user I want an easy to use online app to upload all my own recipes and learn of new recipes shared by other users.
- As a user I want to have my own secure area and be able to easily reference any recipes I have personally added.
- As a user I want to be able to find recipes faster than I would in a traditional cookbook and would like important information regarding allergies to be clearly displayed with the option to exclude recipes which contain certain allergens.
- As a user I want to be able to see information such as, difficulty, time required to prepare and number of servings very quickly to enable me to make decisions quickly and I would also like to be able to select by course type. This is very helpful when planning for dinner parties.

---

To enhance the user experience a more modern one-page theme has been designed. As recipes are added by users new recipe cards are created in the recipes section and stacked using the materialize responsive grid system. The app makes use of flash messaging to confirm to the user when certain actions have been completed e.g. New Recipe Added, Changes Made and/or Recipe Deleted. Pagination has not been used for this project as it was felt that on this occasion scrolling resulted in a better using experience than pagination. Scrolling is faster and is increasingly becoming second nature as a result of mobile devices. Passive Event Listeners have also been introduced in view of this and are new to chrome 51. Cook-e include a CDN to enhance scroll performance on mobile devices.

The application makes use of icons for the nav bar and various options within the app such as add, edit, delete etc… The icons contain relevant images to make their intended purpose clear to the end user. The use of buttons adds more of an App feel as opposed to a more traditional website. For additional clarity tool tips have be utilised so that as the user hovers over a button text is displayed further explaining the action it performs. Animation has also been added to the navigation menu to add to the user experience. A similar effect has been used in the footer for the social media buttons. In mobile view the app returns to a more traditional navigation menu in line with user expectations.

When a user adds a recipe to the app, they can link to an image of the recipe online. If they decide not to do this then a default image will be displayed automatically. This helps to ensure the apps remains aesthetically pleasing and uniform in the event a user opts out of including a photo.

Certain options are only available to users once logged in, for example users who are not logged in will be unable to view the Add, Edit, Delete and Log out buttons. For the scope of this project this is deemed a suitable way to control user access rights although it is recognised that in the real-world further work would need to be conducted on the back end in order to prevent a potential hacking scenario. That said; however, this project goes a lot further than required as part of the project brief in that there is a login and registration page included which was not actually required. User passwords are also encrypted using bcrypt to hash any passwords for extra security.

A user may wish to perform the following actions:

- Browse and Filter recipes in the recipes section
- Register an account
- Add or View individual recipes via the recipes section
- View their own recipes via the recipes section or profile
- Edit or Delete their own recipes
- contact us more traditional means (post/phone/email).
- reach out to us on social media.
- The site provides all these options to the end user and is very easy to use and navigate.

See here for [Wireframes](https://github.com/JayPeaa/milestone4-cook-e/blob/master/Wireframes%20Milestone%204.pdf)


## Database Considerations

Due to the relative simplicity of this app a NoSQL database was selected. The This was the starting point for this data centric project. See here for the [database schema](https://github.com/JayPeaa/milestone4-cook-e/blob/master/static/wireframes_schema/Cook-e%20Schema.pdf)

## Features

The main features of the App are:

- Clear and easy to use navigation
- Good use of colour and modern design
- Fully responsive with a mobile first approach
- An online repository of recipes with Create, Read, Update and Delete functionality
- A contact section, about page and social media channels

## Future developments

Connecting this app to virtual home assistants such as Alexa or Google Home would make Cook-e far more accessible and practical for the modern-day user. Whilst the current registration and login pages go some way towards providing security there is some additional work that would be required which was also outside the scope of this milestone project. This includes adding user profile images and a means to update, reset or delete user accounts and profile information.

Using Ajax and jQuery will allow for instant results when filtering without compromising load speeds which would help to improve the user experience when browsing recipes.

The ability to create a user list of liked recipes as well as the ability to filter by popularity would be a great enhancement to make in the future. In addition to implementing some controls around the like button to only allow registered users to like a recipe and limit the button to one click per user.

Security would need to be enhanced prior to making an app like this live. Security has not been covered in depth in this programmed to this point so whilst this milestone goes further than is required there is still more work to be done.

Forms have been implemented with HTML with categories on select menus referencing the database. This can lead to some vulnerabilities from a security perspective. Utilising WTForms and hard coding form fields where dynamic updating is not required would help protect the underlying database. Course Category is a field which would be enabled to allow users to add their own categories in a future release.

Making this app more social with the ability for users to interact with one another would be a must for an app such as this. This could be achieved with the use of a forum or direct messaging capability.  Including a user image in the profile would also be required as part of this enhancement.

Ability to upload recipe images would be preferable to hotlinking to images online. This was outside the scope of this project but would be a better solution and provide an enhanced user experience.

Data Protections (GDPR) would also need to be given full consideration along with other legalities such as privacy policies, cookie notices and terms of service prior to making such an app available to use.


## Technologies

The site is built using:

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
- [Node Sass](https://github.com/sass/node-sass)
- [jQuery](https://jquery.com/)
- [Materialize](https://materializecss.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Python](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/)
- [Jinja2](http://jinja.pocoo.org/docs/2.10/)

#### CDNs and Library Usage

The following CDNs have been used to create this app.

##### Materialize &amp; Font Awesome

- [https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css](https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css)
- [https://use.fontawesome.com/releases/v5.8.2/css/all.css](https://use.fontawesome.com/releases/v5.8.2/css/all.css)

##### jQuery &amp; Materialize

- [https://code.jquery.com/jquery-3.3.1.min.js](https://code.jquery.com/jquery-3.3.1.min.js)&quot;
- [https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js](https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js)

##### Passive Event Handlers

###### For enhanced scroll performance on mobile

- [https://unpkg.com/default-passive-events](https://unpkg.com/default-passive-events)

## Testing

To ensure any ;form&#39; postings were as anticipated it was common practice to print to the console to determine if the outputs and data structures were as expected. This was done prior to allowing user input to post directly to the database collections.

Recipes were added manually via the front end as part of the testing process which flagged various issues which could then be rectified. During user acceptance testing it became evident that additional controls were required on form inputs to maintain the visual appeal of the app as well as prevent unusual input. Maxlength, Min, Max and required attributes and classes were used to make the app more robust.

Testing has been conducted using google dev tools. Thorough testing in all the various mobile devices along with general responsiveness (responsive mode) has concluded that this site works well in all modern-day browsers and mobile devices. As part of the testing process each page has been reviewed systematically to ensure all links work as intended and the pages display correctly.

This testing has confirmed that users will be able to utilise the app as intended on any device (in landscape or portrait mode) to achieve their goals whilst enjoying the experience and customer journey.

All user forms display correctly and as intended on various displays / devices.

All CSS, HTML and JavaScript was run through code validators and flint to ensure any error were remedied. [Flake8](http://flake8.pycqa.org/en/latest/) was used to ensure that any python code was PEP8 compliant.

### Browser Compatibility Testing

#### Issues Encountered

Time was invested at the start of the project to ensure HTML code and Materialize Classes were working as anticipated which saved some time on responsiveness testing during the latter stages of the build.

HTML and CSS Validators were used to clear any errors, however, HTML validation tends to highlight Jinja2 templating as errors when they are not.

Jshint was utilised to check the quality of any jQuery and it revealed certain variables which were not actually being used which were subsequently removed. There were also various warnings for missing semi colons which have been rectified.

Some minor modifications were made to the layout of my design post wireframing which were straightforward to implement. This was done in order to achieve more balance visually.

Materialize appeared to have a bug with select elements on forms which meant that if drop down fields were left empty there was no feedback for the user and the form would simply not submit. The required and validate classes would normally turn such fields red and display a message on screen. In order to remedy this a custom class was applied with custom CSS styling.

```
.single-selector:required {
  display: block;
  padding: 0;
  position: absolute;
  background: transparent;
  color: transparent;
  border: none;
  top: 0;
  outline: none !important; }
```

During UAT a user successfully hacked the database as a result of a route being hardcoded during the development phase. This vulnerability was subsequently remedied with the use of ```{ url_for }```.

During testing it was identified that users were unable to save two recipes with the same name. This was because two indexes had been created in mongo in error. Once the erroneous index was dropped the system worked as expected.

During mobile testing the add and logout buttons did not appear in the menu as a result of a typo in the jinja formatting. This was subsequently fixed but would have been a sever bug had it not been detected as it would have prevented users from being unable to add recipes.

## Deployment

Throughout the projects regular git commits were made to ensure any working files were backed up. Numerous commits have been logged on the main branch in GitHub. An additional branch was created when working on the login and registration pages. Git checkout was used to switch between branches in the terminal along with push, pull and merge requests to incorporate all change on the main branch following review. Whilst there were no other collaborators on this project it was felt that this represented best practice. It maintained segregation between the registration and login work and the rest of the app. The project has been successfully deployed on [Heroku](https://www.heroku.com/).

AWS cloud9 has been used throughout this project as the IDE of choice.

Issues were encountered when initially deploying the app to Heroku. This was due to Heroku auto detecting Node's package.json file and creating a Node build pack rather than a Python build pack. In order to rectify this issue, the build pack was manually deleted in Heroku and replaced with a python build pack. The package.json file was then removed before pushing the app to Heroku. After the app was successfully deployed to Heroku the package.json file was reinstated.

### File Structure

The project has been organised as follows:

```
ROOT DIRECTORY

milestone4 (Project Folder)
node\_modules (folder)
scss (folder)
static (folder)
templates (folder)
gitignore (file)
license.md (file)
package.json (file)
procfile (file)
readme.md (file)
requirements.txt (file)
run.py (file)
```

The node_modules file includes a number of dependencies which are required to run node sass. This was included in the gitignore file along with package-lock.json.

##### Gitignore

```
node_modules
package-lock.json
```

The [SCSS](https://sass-lang.com/documentation/syntax) folder includes my main.scss file which compiles my CSS. A script is included within my package.json file to run this using the ```run sass``` command.

``` "sass": "node-sass -w scss/ -o static/css/ --recursive"```

The static folder structure is as follows:

```
static (folder)
   CSS (folder)
      main.css (file)
   images (folder)
      (various image files)
   js (folder)
      main.js(file)
   wireframes_schema (folder)
      Cook-e Schema.pdf
      Wireframes Milestone 4.pdf (file)
```

The various pages for this app are in the templates folder. This folder contains the following html templates:

```
templates (folder)
   about.html (file)
   addrecipe.html (file)
   base.html (file)
   contact.html (file)
   editrecipe.html (file)
   instructions.html (file)
   login.html (file)
   profile.html (file)
   recipes.html (file)
   register.html (file)
```

## Credits

### Images and Media

All images and media used on this site have been labelled for reuse / non-commercial and are for educational purposes only. Google images licensing tools have been utilised in sourcing content.

The favicon was generated by a 3rd party site: [https://favicon.io/favicon-generator/](https://favicon.io/favicon-generator/).

Special thanks to the Code Institute Slack Community, CI Tutors and project mentor Tony Montaro for support and guidance provided during this project.

## Licensing 

Released with MIT licensing rights 