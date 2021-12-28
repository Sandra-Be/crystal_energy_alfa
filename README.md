# Crystal Energy

![Crystal Energy](project_files/website/.jpg "Crystal Energy")

* [Click here](https://.herokuapp.com/) and view the live project.

# Table of contents

1. [Introduction](#Introduction)
2. [UX](#UX)
   * [Strategy](#Strategy)
      * [Website strategy](#Website-strategy)
      * [Target audience](#Target-audience)
      * [External Visitor's goal's](#External-Visitor's-goal's)
      * [Ideal client](#Ideal-client)
      * [Site Owner's goal's](#Site-Owner's-goal's)
   * [Scope](#Scope)
      * [User stories](#User-stories)
      * [Features](#Features)
   * [Structure](#Structure)
      * [Site structure](#Site-structure)
   * [Skeleton](#Skeleton)
      * [Quick sketch](#Quick-sketch)
      * [Wireframes](#Wireframes)
   * [Design](#Design)
      * [Colour scheme](#Colour-scheme)
      * [Fonts](#Fonts)
      * [Media](#Media)
      * [Languages](#Languages)
      * [Technologies Used](#Technologies-Used) 
3. [Completed Live Site](#Completed-Live-Site)
   * [Existing features](#Existing-features) 
   * [Features to Implement in future](#Features-to-Implement-in-future)  
4. [Testing](#Testing)
   * [W3C Validation](#W3C-Validation)
   * [Jshint Validation](#Jshint-Validation)
   * [PEP8 Validation](#PEP8-Validation)
   * [User stories testing](#User-stories-testing)
   * [Functional testing](#Function-testing)
5. [Database Design](#Database-Design)
   * [Database schema](#Database-schema)
6. [Deployment](#Deployment)
   * [MongoDB Configuration](#MongoDB-Configuration)
   * [Heroku Deployment](#Heroku-Deployment)
   * [Forking the Repository](#Forking-the-Repository)
   * [Creating a Clone](#Creating-a-Clone)
7. [Credits](#Credits)
   * [Images and text](#Images-and-text)
   * [Helpfull sites](#Helpfull-sites)
   * [Acknowledgements](#Acknowledgements)

# Introduction



# UX

## Strategy
### Website strategy



![Strategy](project_files/website/strategy_3.jpg "Strategy")

### Target audience

* People seeking a spiritual path
* People seeking inspiration

### External Visitor's goal's



### Ideal client

* A person who is free thinking
* A person who is spiritualy aware
* A person who wants to broaden there horizons
* A person who is seeking a like minded community

### Site Owner's goal's



## Scope
### User stories



### Features



## Structure

### Site structure

![Structure](project_files/website/structure_magic.jpg "Structure")

## Skeleton
### Quick sketch

![Quick sketch](project_files/website/sketch.jpg "Quick sketch")

### Wireframes

View of the main home page for website:

![Wireframes](project_files/wireframes/wireframes_magic.png "Wireframes") 

Views of the rest pages on website:



## Design
### Colour scheme

Colours of ... [mycolor.space](http://mycolor.space) is used throughout site.

![Colour palette](project_files/website/colours.jpg "Colour palette")

### Fonts



### Media



### Languages

This project uses [HTML5](https://en.wikipedia.org/wiki/HTML5) Hypertext Markup Language (HTML), [CSS3](https://en.wikipedia.org/wiki/CSS) Cascading Style Sheets (CSS), [jQ](https://en.wikipedia.org/wiki/JQuery) jQuery (jQuery) and [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) Python.

### Technologies Used

* [BSON](https://bsonspec.org/) - bson.objectid is a required dependency for MongoDB management system.
* [MongoDB](https://www.mongodb.com/) - used for database functionality.
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - used to host the database.
* [mycolor.space](http://mycolor.space) - used for colour palette throughout the site.
* [Google Fonts](https://fonts.google.com/) - were used throughout the site.
* Icons on website were added with [Font Awesome](https://fontawesome.com/).
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - framework used to create and populate the templates.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Jinja templating language was used to simplify and display backend data in html.
* [JQuery](https://jquery.com/) - used to activate the Materialize functionality.
* [PyMongo](https://pypi.org/project/pymongo/) - flask_pymongo used for interacting with MongoDB database from Python.
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - used for password hashing and authentication.
* [Git](https://git-scm.com/) - used for version control to commit to Git and push to Heroku.
* Project code stored on [GitHub](https://github.com/).
* [gitpod.io](https://gitpod.io/workspaces) was used for coding.
* [Heroku](https://www.heroku.com/home) - cloud platform used to deploy application.
* [PEP8](https://www.python.org/dev/peps/pep-0008/) - used to check code for PEP8 requirements.
* [PEP8online](http://pep8online.com/) - used to check code for PEP8 requirements.
* [RandomKeygen](https://randomkeygen.com/) - used to generate secure password to Secret Key.
* Wireframes were created on [Balsamiq](https://balsamiq.com/).
* [Am I Responsive!](http://ami.responsivedesign.is/) website to review projects responsiveness.
* [jshint.com](http://jshint.com) used for jQuery code validation.
* [W3C Markup Validation Service](https://validator.w3.org/) used for HTML code validation.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) used for CSS code validation.

# Completed Live Site

![Website Layout](project_files/website/website_layout.jpg "Website Layout")

* [Click here](https://magic-spells-project.herokuapp.com/) and view the live site.

## Existing features 



## Features to Implement in future



# Testing



## W3C Validation

To validate every page of the project, that there were no syntax errors, these two Validators were used, W3C Validator and W3C CSS Validator.
To make make it easier to validate html code, since using jinja templating language throughout all pages, which results in errors in online validators. I used URL address.
For W3C Css Validator I copied css code directly.

* [W3C Validator](project_files/validators/w3c.jpg "W3C Validator")
* [W3C CSS Validator](project_files/validators/W3c_css.pdf "W3C CSS Validator")

## Jshint Validation

For this project I used jQuery - JavaScript Library for MaterializeCSS initialization: "Write less, do more."
Jshint were used to validate jQuery file of this project. [Click](project_files/validators/jshint.jpg) to view report.

## PEP8 Validation

Python code checked for PEP8 requirements. [Click](project_files/validators/pep8.jpg) to view report.

## User stories testing
   
   
## Functional testing

Throughout the website every link, field and icon was tested and all results are displayed on the table below:

| Location | Type | Expected Result | Actual Result | Pass/Fail/Not executed|
| :----: | :----: | :----: | :----: | :----: |


# Database Design

MongoDB Atlas is used as database backend for storing user and spells details. There are three collections.

## Database schema

![Database Schema](project_files/website/shema.jpg "Database Schema")

# Deployment

## MongoDB Configuration

1. Login to your [MongoDB](https://www.mongodb.com/) Account.
2. From Clusters tab, click on Connect.
3. Select Connect to your application.
4. Select Python as Driver and choose Version 3.6 or later
5. Create a new env python file in your project, paste and save the connection link and variables.

![Link](project_files/website/link_snippet.jpg "Link")

6. Create an instance of PyMongo.

![Link](project_files/website/link_snippet1.jpg "Link")

## Heroku Deployment

1. Before deploying your project create a requirements.txt file by running the following command in the CLI:

![Command](project_files/website/command1.jpg "Command")

2. Create a Procfile file by running the following command in the CLI:

![Command](project_files/website/command2.jpg "Command")

3. git add and git commit the new requirements and Procfile and then git push the project to GitHub.
4. Log in to [Heroku](https://id.heroku.com/login).
5. Select "New" on your dashboard and then select "Create new app".
6. Choose a name for your application, select your region, and then click "Create app".
7. From the app dashboard, navigate to "Deploy" tab.
8. From Deployment method select "Github" and confirm the linking of the Heroku app by clicking "Search" then select your repository name.
9. Once you select your repository, click on "Connect".
10. After you connected to your repository, click on "Settings" tab on your app dashboard, and click on "Reveal Config Vars" and add your configuration variables to Heroku.
11. Navigate to "Deploy" tab, and from Manual deploy choose your master branch, and click "Deploy Branch".
12. After you deployed your branch "Enable Automatic Deploys".
13. Site is successfully deployed, any further changes will automatically be updated everytime they are commited and pushed on Github.

## Forking the GitHub Repository

1. Log into [GitHub](https://github.com/) or [create an account](https://github.com/).
2. Locate the [GitHub Repository](https://github.com/Sandra-Be/).
3. At the top of the repository, on the right side of the page, select "Fork".
4. You should now have a copy of the original repository in your GitHub account.

## Creating a Clone

1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension) Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/) or [create an account](https://github.com/).
4. Locate the [GitHub Repository](https://github.com/Sandra-Be/).
5. Click the green "GitPod" button in the top right corner of the repository. This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

### How to run this project within a local IDE, such as VSCode

1. Log into [GitHub](https://github.com/) or [create an account](https://github.com/).
2. Locate the [GitHub Repository](https://github.com/Sandra-Be/).
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.

   > git clone https://github.com/USERNAME/REPOSITORY

8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

# Credits

## Images and text



## Helpfull sites

* [stackoverflow.com](https://stackoverflow.com/) - website for code tips.
* [learn.codeinstutute.net](https://learn.codeinstitute.net/login?next=/) - HTML, CSS, JavaScript and Python study materials.
* [www.markdownguide.org](https://www.markdownguide.org/basic-syntax) - useful website for Markdown language creating README.md file.

## Acknowledgements 

* My mentor Dick Vlaanderen for helpful feedback.
* Student support at Code Institute Slack platform for their support.