# Milestone Project 4 
#### Data Centric Development
#### Design and Build an Interactive Cooking App.
---

### App Name: Cook-e

##### Deployment: https://cook-e.herokuapp.com/

Cook-e is an interactive cooking app which allows users to share recipes online. It enables users to browse recipes uploaded by other users as well as add, edit and delete their own recipes.  This app is built using Flask and MongoDB, a NoSQL or document store database but incorporates a number or other technologies.

Having recipes stored on line in a system which allows users to filter and quickly reference their own personal recipes at the click of a button is infinitely faster than using traditional cookbooks.  In addition with the advent of tablets and virtual assistants such as google home, more and more users are making use of digital media when preparing meals in the home. 

---

## UX
The UX has been designed with the end user in mind and as expectations in terms of front end design are ever increasing I opted to utilise Materialize.css for my design and responive layout.  Materialize.css is a library of UI components desinged by Google with the aim of providing a unified and consistent user experience.

#### User Stories

* As the app developer I want to build an app which allowed users to share recipes in one convienient location.
* As the app developer I want these recipes to be presented in a user friendly and secure way which allowed users to only edit or delete their own recipes.
* As the app developer I want to create an app which was very viusal with quirky animation and a move away from a traditional text based navigation menu.
* As a user I want an easy to use online app to upload all my own recipes and learn of new recipes shared by other users.
* As a user I want to have my own secure area and be able to eaily reference any recipes I have personally added.
* As a user I want to be able to find recipes faster than I would in a traditional cookbook and would like important information regarding allergies to be cleary displayed with the option to exclude recipes which contain certain allergens.
* As a user I want to be able to see information such as, difficulty, time required toprepare and number of servings very quickly to enable me to make decisions quickly and I would also like to be able to select by course type.  This is very helpful when planning for dinner parties.

To enhance the user experience a more modern one-page theme has been designed. As recipes are added by users new recipe cards are created in the recipes section and stacked using the materialize responsive grid system. The app makes use of flash messaging to confirm to the user when certain actions have been completed e.g. New Recipe Added,  Changes Made and/or Recipe Deleted. Pagination has not been used for this project as it was felt that on this occassion scolling resulted in a better using experience than pagination.  Scrolling is faster and is increasingly becoming sencond nature as a result of mobile devices. Passive Event Lisenters have also been introduced in view of this and are new to chrome 51.  Cook-e include a CDN to enhance scroll performance on mobile devices.

The application makes use of icons for the nav bar and various options within the app such as add, edit, delete etc.. The icons contain relevant images to make their intended purpose clear to the end user.  The use of buttons adds more of an 'App' feel as opposed to a more traditional website.  For aditional clarity tool tips have be utilised so that as the user hovers over a particular button text is displayed further explaining the action it performs. Animation has also been added to the navigation menue to add to the user experience.  A similar effect has been use in the footer for the social media buttons. In mobile view the app returns to a more traditional navigation menu in line with user expactaitions.

When a user adds a recipe to the app they can decide to link to an image of the recipe.  If they decide not to do this then a default image will be displayed automatically.  This helps to ensure the apps remains aestetically pleasing and uniform in the event a users opps out of adding a photo.  

Certain options are only avialbe to users once logged in, for example users who are not logged in will be unable to view the Add, Edit, Delete and Log out buttons.  For the scope of this project this is deemed a suitable way to control user access rights although it is recognised that in the real world futher work would need to be conducted on the back end in order to prevent a potential 'hacking' scenario.  That said, however, this project goes a lot further than required as part of the project brief in that there is a login and registration page included which was not actually required.  User passwords are also encrypted using brypt to hash any passwords for extra security.  

A user may wish to perform the following actions:

* Browse and Filter recipes in the recipes section
* Register an account
* Add or View individual recipes via the recipes section
* View their own recipes via the recipes section or profile
* Edit or Delete their own recipes
* contact us more traditional means (post/phone/email).
* reach out to us on social media.
* The site provides all these options to the end user and is very easy to use and navigate.

Wireframes for this project are available here https://github.com/JayPeaa/milestone4-cook-e/blob/master/Wireframes%20Milestone%204.pdf

##Features
The main features of the App are:

*Clear and easy to use navigation
*Good use of colour and modern design
*Fully responsive with a mobile first approach
*An online repository of recipes with Create, Read, Update and Delete functionality
*A contact section, about page and social media channels

##Future development

Connecting this app to virtual home assistants such as Alexa or Google Home would make Cook-e far more accessible and practicle for the modern day user.
Whilst the current registration and login pages go someway towards providing security there is some additional work that would be required which was also outside the scope of this milestone project.  This includes adding user profile images and a means to update, reset or delete user accounts and profile information.

Using Ajax and JQuery will allow for instant results when filtering without compromising load speeds which would help to improve the user experience when browsing recipes.

##Technologies
The site is built using HTML, CSS, NodeSass, JavaScript, jQuery, Materialize, Flask, Python and mongoDB.  It also makes use of the Jinja2 templating language. Usage of any libraries or CDNs is documented below:

CDN Usages
The following CDNs have been used to create this site.

https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css
https://use.fontawesome.com/releases/v5.8.2/css/all.css

Libraries
https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous" https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js

Testing
To ensure any form postings were as anticipated it was common practice to pprint to the consol priror to allowing form to post directly to the database collection.

Testing has been conducted using google dev tools. Thorough testing in all the various mobile devices along with general responsiveness (responsive mode) has concluded that this site works well in all modern-day browsers and mobile devices. As part of the testing process each page has been reviewed systematically to ensure all links work as intended and the pages display correctly.

This testing has confirmed that users will be able to utilise the app as intended on any device (in landscape or portrait mode) to achieve their goals whilst enjoying the experience and customer journey.

All user forms display correctly and as intended on various displays / devices.

Autoprefixer was used to ensure CSS is compatible in multiple browsers: https://autoprefixer.github.io/

A common approach to testing code was to print to the console. This was particularly useful for testing conditions prior to adding additional code and for viewing variable or array values.

All CSS, HTML and JavaScript was run through code validators and flint to ensure any error were remedied.

Browser Compatibility Testing:
Issues Encountered
Time was invested at the start of the project to ensure HTML code and Materialize Classes were working as anticipated which saved some time on responsiveness testing during the latter stages of the build. 

HTML and CSS Validators were used to clear any errors, however, CSS validation tends to highlight browser extensions as errors when they are actually required.

Jshint was utilised to check the quality of any Javascrip and jQuery and it revealed certain variables which were not actually being used which were subsequently removed. There were also various warnings for missing semi colons which have been rectified.

Some minor modifications were made to the layout of my design post wireframing which were straightforward to implement. This was done in order to achieve more balance visually.

UPDATE TESTING ****************

Internet Explorer does not support the Linear Gradient CSS property and consequently the background image did not display. To fix this issue the header iamge was edited outside of CSS using PINETOOLS editing online (https://pinetools.com/darken-image). Internet Explorer also required anditional CSS in order to display the various buttons on the page correctly (Position Relative) which was not required for any other browser.


Deployment
Throughout the projects regular git commits were made to ensure any working files were backed up. Numerous commits have been logged on the main branch in GitHub. The project has been successfully deployed on GitHub pages.
An aditional branch was created when working on the login and registration pages.  Git checkout was used to swith branches in the terminal along with push, pull and merge requests to incorporate all change on the main branch following review. 

AWS cloud9 has been used throughout this project as the IDE of choice.

Issues were encountered when initially deploying the app to Heroku. This was due to Heroku detecing auto detecing Node and creating a Node Buildpack rather than a Python Buildpack. This was due to using Node Sass and including a package.json file as a result.  In order to rectify this the buildpack was manually deleted in Heroku and a python build pack was manually added.  The package.json file was then removed before pushing the app to Heroku.  After the app was successfully deployed the package.json file was reinstated.

UPDATE NEED FROM HERE DOWN:*********************

File Structure
The project has been organised in the following structure:

milestone2 (Project Folder)
assets (folder)
css (folder)
data (folder)
davicon
js (folder)
vendor (folder)
images (folder)
video (folder)
Index.html and Readme.md are both located in the main project folder as are the wireframes for the initial design.

The vendor folder contains any 3rd party assets such as photos, video and audio materials for which proper approval has been attained prior to use.

Credits
The favicon was generated by a 3rd party site: https://favicon.io/favicon-generator/.

Images and Media
All images and media used on this site have been labelled for reuse / non-commercial and are for educational purposes only. Google images licensing tools have been utilised in sourcing content. Express consent has been attained via email for any other 3rd party content namely the video.