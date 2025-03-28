# Flask resource keeper app
## Code Institute portfolio project
### Technologies
- Flask
- PostgeSQL
- Bootstrap
- Heroku
 ![screenshot](documentation/images/features-homepage.png)
# Overview
* Resource Keeper is a flask app that allows users to store and retrieve references and resources (as urls) in a SQL relational database.
* The rationale and design strategy for the app comes from my own experience of finding a solution to keep online resources in a an organized way.
* The app is intended for use by students or anyone that wants a simple way to keep url resources in a database.
* Users are able to view saved resources by category and see a short description of the resource.
* The database stores the url for each resource and users can go straight from the list view to the visit the resource.
* Users are able to create categories and add resources to the categories for future reference.
* Users are able to edit and delete both categories and resources
* The app demonstrates basic database CRUD operations where users can create records, view records, update and delete records.
* The app provides immediate visual confimation of database CRUD operations. 
* The app provides a simple attractive interface based on the Bootstrap 5 framework.

## User Stories
* User stories are based on the intended scope of the app as described above. The user stories below, were also used to test the app functionality.

|User action |
|--------|
| As a site user, I would like to create a new category
| As a site user, I would like to create a new resource within a category
| As a site user, I would like to view existing categories
| As a site user, I would like to view stored resources by category with a short note describing the resource.
| As a site user, I would like to be able to access a resource (ie go to that url).
| As a site user, I would like to be able to edit a resource details.
| As a site user, I would like to be able to edit a category name
| As a site user, I would like to be able to move a resource to a different category
| As a site user, I would like to be able to delete a resource
| As a site user, I would like to be able to delete a category
| As a site user, I would like to have custom error pages (http error codes 500 and 404) displayed where appropriate
| As a site user, I would like to be able to easily return to home page via main navigation.
| As a site user, I would like immediate visual feedback when creating a new category
| As a site user, I would like immediate visual feedback when creating a new resource
| As a site user, I would like immediate visual feedback when deleting a category
| As a site user, I would like immediate visual feedback when deleting a resource
| As a site user, I would like immediate visual feedback when updating a category
| As a site user, I would like immediate visual feedback when updating resource details
||

## Wireframes
| Page | Device | Wireframe |
| --- | --- | --- |
| Home | Desktop | [wireframe](documentation/wireframes/home-dt.jpg) |
| Home | Mobile | [wireframe](documentation/wireframes/home-mo.jpg) |
| Edit category | Desktop | [wireframe](documentation/wireframes/ed-cat-dt.jpg) |
| Edit category | Mobile | [wireframe](documentation/wireframes/ed-cat-mo.jpg) |
| Add resource | Desktop | [wireframe](documentation/wireframes/add-res-dt.jpg) |
| Add resource | Mobile | [wireframe](documentation/wireframes/ed-res-mo.jpg) |
| View resource | Desktop | [wireframe](documentation/wireframes/view-res-dt.jpg) |
| View resource | Mobile | [wireframe](documentation/wireframes/view-res-mo.jpg) |
| Edit resource | Desktop | [wireframe](documentation/wireframes/ed-res-dt.jpg) |
| Edit resource | Mobile | [wireframe](documentation/wireframes/ed-res-mo.jpg) |


## Features
- The features included were intended to realize the user stories detailed above.
### Home Page View
- General view shown below shows main navigation (which is included on all pages)and the button to go to the "add category" view. Also shown are cards showing existing resource categories in the database. 
- ![screenshot](documentation/images/features-homepage.png)
- The "New Category" button takes the user to a view to add a new category.
- ![screenshot](documentation/images/features-new-category-button.png)
- Existing category cards have buttons to go to views to view resources in the category, to add a new resource to the category, and to edit the category.
- ![screenshot](documentation/images/features-cards.png)
### Add New Category View
- This view is accessed via the "New Category" button shown above. The view provides an input form for the user to create a new category and add this to the database
- ![screenshot](documentation/images/features-add-category.png)
### View Stored Resources
- This view is accessed via the "view" button in the category cards shown above. The view provides a list of the resources for a given category. A link is provided to go to the resource url. A "details" dropdown on-hover, shows a short description of the resource from the database. An "edit" button takes the user to the view to edit the resource.
- ![screenshot](documentation/images/features-view-resources.png)
### Edit Category View
- This view is accessed via the "edit" button on the category card. The view provides an input form for the user to edit the name or delete an existing category. The current category name is shown in a disabled field for reference.
- ![screenshot](documentation/images/features-edit-category.png)
### Delete Category View
- If the user choses to delete a category in the view for editing the category, a pop-up modal is fired to confirm the deletion
- ![screenshot](documentation/images/features-delete-category-modal.png)
### Add New Resource View
- This view is accessed via the "add" button on the category card. The view provides an input form for the user to add the details of a new resource and a button to add the resource to the  database.
- ![screenshot](documentation/images/features-add-resource.png)
### Edit Existing Resource View
- This view is accessed via the "edit" button in the "View stored Resources View" shown above. The view provides an input form for the user to edit the details of an existing resource and a button to add the new resource details to the  database. The delete button provides the option to delete the resource from the database.
- ![screenshot](documentation/images/features-edit-resource.png)
### Delete Resource View
- If the user chooses to delete a resource in the view for editing the resource, a pop-up modal is fired to confirm the deletion.
- ![screenshot](documentation/images/features-delete-resource-modal.png)

### 404 Error Page
- If the user makes a request to a non-existent route a 404 error page is displayed. A back link is provided to return to the homepage.
- ![screenshot](documentation/images/features-404.png)

### 500 Error Page
- In case of a server error a page informing the user is provided with a link back to homepage
- ![screenshot](documentation/images/defence-500.png)

## UX
#### Colour palette 
An attractive coherent color palette for the site was chosen from [Colorhunt](https://colorhunt.co/palette/b80257dd356efc7fb6ffbbe1) and is shown below.

![screenshot](documentation/images/colorPalette.png)

#### Typography
 [Barlow](https://fonts.google.com/specimen/Barlow?query=barlow) font was used for all site text.

## Tools & Technologies Used
- [Python](https://www.python.org/) used to code flask server and interact with database.
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) used as the backend python framework.
- [Flask-Sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) used to provide object-oriented interaction with SQL database.
- [PostgreSql](https://www.postgresql.org/) used for database management.
- [Heroku](https://www.heroku.com/) flask application hosting.
- [ElephantSQL](https://www.elephantsql.com/) database hosting.
- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for responsive layout.
- [JavaScript](https://www.javascript.com) included for correct functioning of Bootstrap components.
- [Git](https://git-scm.com) used for version control, continuous deployment to Heroku and hosting video assets. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [VSCode](https://code.visualstudio.com/) IDE for development work.
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) used in html templates.
- [Code Institute Python PEP8 Linter](https://peps.python.org/pep-0008/) Used to check python code for pep8 compliance.
## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment
### Cloud Deployment
The app was deployed to the Heroku [Heroku](https://www.heroku.com/) cloud platform, and the database was deployed to the [ElephantSQL](https://www.elephantsql.com/) PostgreSQL as a service provider
### Deployment to Heroku
1. Generate the requirements.txt file with the following command in the terminal. After you run this command a new file called requirements.txt should appear in your root directory `pip3 freeze --local > requirements.txt`.
2. Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it
3. Inside the file, add the following command, `web: python run.py`
4. Save all your files and then add, commit and push your changes to GitHub
5. Log into Heroku.com and click “New” and then “Create a new app”
6. Choose a unique name for your app, select the region closest to you and click “Create app”
7. Go to the Settings tab of your new app and click "Reveal Config Vars".
8. Add a Config Var called DATABASE_URL and paste your database URL in as the value. 
9. Add remaining Config Var's as required
10. In Heroku navigate to the “Deploy” tab of your app and in the Deployment method section, select “Connect to GitHub”
11. To allow deployment on pushing to Github select Enable Automatic Deploys.
12. To enable database start by clicking the “More” button and select “Run console”.
13. Enable python3 console and enter the following to dreate database tables.

```python
from taskmanager import db
db.create_all()
```

14. To open app click the “Open app” button

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/doctorandrewbrown/flask-resource-keeper) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	```bash
    git clone https://github.com/doctorandrewbrown/flask-resource-keeper.git
    ```
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/?autostart=true#https://github.com/doctorandrewbrown/flask-resource-keeper)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/doctorandrewbrown/flask-resource-keeper.git)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Security
The following basic security measures were taken to protect the deployed app.
- The ```debug``` parameter was set to ```False``` in the heroku (production) version of the ```run.py``` file
(in the local development version ```debug``` can be set to ```True``` for development purposes).
```python
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        # Set debug to dev or production mode
        debug=False
    )
```
- For local development purposes, `environment variables` were stored in the `env.py` file. This file includes a value for `SECRET KEY` which must not be exposed in the github repository. For this reason `env.py` is included in the `.gitignore` file so it is not pushed to Github. 
- Environment variables needed by the app were securely set in the `config vars` section in Heroku dashboard when logged into the account. Here, the value of `SECRET KEY` was set and the value of the `DEBUG` key was set to`False`.
## Bugs
### Unwanted stretching of edit button
- The default behaviour of the button is to stretch to fill the height of containing row as shown
![screenshot](documentation/images/bugs-button-stretch.png)
- This unwanted effect was corrected by including the attribute `style="align-self:self-start;"` on the button element
![screenshot](documentation/images/bugs-button-stretch-corrected.png)

There are no bugs remaining that I am aware of.

## Credits
### Media 
| Source | Location | Notes |
| --- | --- | --- |
| [Favicon.io](https://favicon.io/favicon-generator/) | index.html | used to generate website favicon  |

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [W3Schools](https://www.w3schools.com/) | whole site | reference for bootstrap, html, css, javascript and python |
| [Markdown Guide](https://www.markdownguide.org/cheat-sheet/) | README and TESTING | syntax guide for writing Markdown files |
| [Html Dropdown](https://www.w3schools.com/css/tryit.asp?filename=trycss_dropdown_text) | edit resource view | Html form dropdown to choose category |
| [Html max-length attribute](https://www.w3schools.com/tags/att_input_maxlength.asp) | input forms | attribute to limit form input length |
| [Html form default value](https://linuxhint.com/add-default-value-for-html-textarea/)| input form view | add placeholder to form fields |
| [Flask error messages](https://www.digitalocean.com/community/tutorials/how-to-handle-errors-in-a-flask-application) | routes.py | Use of flask error messages|
| [Bootstrap Modal](https://www.w3schools.com/bootstrap5/bootstrap_modal.php) | edit category and resources views| Prompt confirmation of deletion from database |
| [Prevent unwanted flexing of bootstrap components](https://www.devsamples.com/css/flexbox-prevent-element-stretching) |resources view| Prevent unwanted flexing of buttons |
| [Github video uoloads](https://github.blog/2021-05-13-video-uploads-available-github/) |documentation| How to include MP4 video |



### Acknowledgements

- I would like to thank my Code Institute mentor, Antonio Rodriguez, and Iris Smok of Code Institute, for their help and advice while developing this project. 
