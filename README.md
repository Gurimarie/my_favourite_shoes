README-file- template

# "I Love Shoes"
## A web-site where shoe-lovers may share, discuss and talk about their favourite shoes 
Looking through the public gallery is open to anyone visiting the site, but in order to contribute to the database, you need to create a user and log in.

When entering a record for a pair of shoes, you may choose for it to be public (visible to everyone), og private (only visible on your private profile-page).

![Picture of different view-port-displays](assets/images/love_shoes_responsive.JPG)

Click here to view the website http://i-love-shoes.herokuapp.com/home_page

## User Experience (UX)

### User stories:

### First time visitor goals
Exploring the site and getting inspired.

### Returning visitor goals
Register as a user, start to build my profile, or just get inspiration from others. Finding out if those beatiful deasigner-shoes I've dreamt about are actually comfortable to wear (or just pretty to look at), from someone who has already bought them.

### Frequent user goals
Sharing and getting followers. Perhaps promoting small shoe-brands?
May also be just for private use, keeping a record of all my shoes, to go through when I need to decide what to wear, or what I need to buy for the next season.

### Site owner goals
Get information on what shoelovers appreciate most in their shoes, and what variables should be available to choose from if the users were to design their own favourite shoes. Ultimately to create a "design-your-own-shoes"-shoe-brand.

## Design

### Colour scheme:
https://materializecss.com/color.html
- navbar: grey darken-4
- background: grey lighten-4
- submit/enter buttons: light-blue darken-4
- cancel/reset buttons: green darken-2
- flash: blue lighten-3
- delete buttons: pink darken-2

![Picture of colour scheme](assets/images/love_shoes_colors.JPG)


### Imagery:
- All images are from https://www.pexels.com/search/shoes/


## Features

- Register a user, with access to private profile-page
- User passwords are hashed using "Werkzeug"
- CRUD Create, read, update and delete records of shoes in the database 
- Create, update and delete records of categories in the database, only for admin-user
- Search-function on Gallery-page, searching through words in "shoe-name" and "shoe-description".


#### Future features:
- We collect user email at registration, and plan to set up a password-recovery-system by way of email.
- Users should be able to "like" and comment on each others pictures/shoe-records.
- There should be filters on the gallery-page, filtering by category, heel-height or comfort-level and all the other features, in addition to the word-search that is there now.



## Technology used
### Programming languages:
- html
- css
- JavaScript
- Python + Flask (flask pymongo)
- MongoDB
- jQuery

### Frameworks, libraries and programs:
- MaterializeCss https://materializecss.com
- RandomKeyGem (for secret_key) https://randomkeygen.com/
- Werkzeug Security Helpers (for user password-hashing)
https://werkzeug.palletsprojects.com/en/2.0.x/utils/#module-werkzeug.security


## Testing

### Validation:
## HTML validation
Lack of alt-attribute for images cane up as an error, and has been fixed.

JS validation


### Testing for user stories in UX-section:
Everything has been tested every step of the way.

### Further testing:
#### Test on different screen sizes:
The Logo in the navbar was too large on small devices, so it has been given the class of "hide-on-med-and-down" so that it is not visible on smaller devices anymore.

#### Test on different browsers:
The website has been tested on Chrome and Firefox, and works fine on both. 

### Fixed bugs:
#### Bug 1
The Logo in the navbar was too large on small devices, so it has been given the class of "hide-on-med-and-down" so that it is not visible on smaller devices anymore.

#### Bug 2
The "toe_shape"-feature did not register in the database when entering new shoe-records. It turned out to be because of inconsistent use of "toe_shape" and "toe-shape". Once there were underscores everywhere and no dashes, it worked fine.


### Unfixed bugs:
When editing a shoe-record, the current value on every field should be collected from the database, but I have not yet figured out how to do that for the two select-input-fields "heel_height" and "toe_shape". Therefore these fields are empty when we start to edit, and if they are not filled in, the prior value is overwritten by the empty input. This should be fixed both by successfully retrieving the data, and also by some rule that an empty new value should not overwrite a prior value.


## Deployment
This project was developed using Gitpod.io with the basic template from Code Institute. Committed to git and pushed to GitHub using git-extensions in Github.
The database used is Cloud MongoDB. I first created the database on the MongoDB-website, and then connected it to the project through the Mongo_URI.
The project was then deployed at Heroku.com with automatic deploys through github.


### Forking the GitHub repository:

### Making a local clone:
1. Follow this link (https://github.com/Gurimarie/my_favourite_shoes) to the projects Github repository.
2. Under the repository name, click the green "Code"-button, and choose "https" and click on the "Download Zip"-option.
3. When the zip is downloaded, open the folder, and move the unzipped folder to where you wish to store it on your computer.
4. Open your Visual Studio Code (or other programming-software), click File, Open Folder, and choose the unzipped folder you just downloaded from where you saved it to.
 



## Credits

### Code:

- https://github.com/PaulFrankling/discover-north-yorks used for README-structure.
- This project follows closely the Flask Mini-project from Module 3, Code Institute. The details are different but that project has been a template for the development of is project.


### Media used:
- All images are from https://www.pexels.com/search/shoes/ (free image-base)


