# Flask resource keeper app

## [Live site here](https://resource-keeper-9faa6ecfb87f.herokuapp.com/)
# Overview
* Resource Keeper is a flask app that allows users to store and retrieve references and resources (as urls) in a SQL relational database.
* The rationale and design strategy for the app comes from my own experience of finding a solution to keep online resources in a an organized way.
* The app is intended for use by students or anyone that wants a simple way to keep url resources in a database.
* Users are able to view saved resources by category and see a short description of the resource.
* The database stores the url for each resource and users can go straight from the list to the visit the resource.
* Users are able to create categories and add resources to the categories for future reference.
* Users are able to edit and delete both categories and resources
* The app demonstrates basic database CRUD operations in that users can create records, view records, update and delete records.
* The app provides a simple attractive interface based on the Bootstrap 5 framework.

## User Stories
* User stories are based on the intended scope of the app as described above. The user stories below, were also used to test the app functionality.

|User action |
|--------|
| As a site user, I would like to create a new resource category
| As a site user, I would like to create a new resource within the category
| As a site user, I would like to view existing categories
| As a retuning site user, I would like to view stored resources by category with a short note describing the resource.
| As a site user, I would like to be able to access a resource.
| As a site user, I would like to be able to edit a resource (ie go to that url)
| As a site user, I would like to be able to edit a category name
| As a site user, I would like to be able to move a resource to a different category
| As a site user, I would like to be able to delete a resource
| As a site user, I would like to be able to delete a category
||
## Features
- The features included were intended to serve the user stories detailed above.
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
### View Stored Resources View
- This view is accessed via the "view" button in the category cards shown above. The view provides a list of the resources for a given category. A link is provided to go to the resource url. A "details" dropdown on-hover, shows a short description of the resource from the database. An "edit" button takes the user to the view to edit the resource.
- ![screenshot](documentation/images/features-resources-view.png)
### Edit Category View
- This view is accessed via the "edit" button on the category card. The view provides an input form for the user to edit the name or delete an existing category. The current category name is shown for reference.
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








## [video](documentation/TEST.mp4)

## UX
#### Colour palette 
An attractive coherent color palette for the site was generated using [Colorhunt](https://colorhunt.co/palette/b80257dd356efc7fb6ffbbe1) and is shown below.

![screenshot](documentation/images/colorPalette.png)

#### Typography
 [Barlow](https://fonts.google.com/specimen/Barlow?query=barlow) font was used for all site text.
