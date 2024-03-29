# GameHoard Website Project with Python and Django Framework
This website was created using the django framework. Its theme is that of an online 'game cubbard'. 
It lets users create and update records of the games they own, add and remove items from a wishlist, 
read reviews generated by web scraping with beautifulsoup, and search API results based on user input.

## Skills Implemented
- <b>Languages:</b> HTML and XML, Python, Django Template Language, JavaScript, CSS.
- <b>Agile project management:</b> created and submitted successive iterations of the app, adding features and functionality with each generation.
- <b>Azure Dev Ops:</b> collaborated with team members to plan and track code assignments.
- <b>Git and PyCharm Version Control:</b> coordinated branching and push requests to record changes to the project over time and avoid code conflicts.
- <b>Django Framework:</b> implemented the Model-View-Template architecture. Leveraged django tags to include content throughout multiple templates. Implemented models and forms to both collect and display information. 
- <b>BeautifulSoup:</b> extracted data from HTML and XML documents by parsing with the beautifulsoup python library. BeautifulSoup source content credit: [BoardGameQuest](https://www.boardgamequest.com/category/game-reviews/)
- <b>API:</b> submitted application programming interface requests to gather content and to return results based on user input. API source content credit:  [CheapShark](https://apidocs.cheapshark.com/#c33f57dd-3bb3-3b1f-c454-08cab413a115)
- <b>Google:</b> debugged code using multiple online resources.
 
## Sprint Overview
During a two-week sprint, team members were tasked with completing various front and back end features to produce a viable app to be included as part of an online portfolio. 
The sprint was real-world experience as part of a large, multi-person group project. 
Specific tasks were assigned by the sprint leader, to be completed within a certain timeframe and meeting set parameters.
- Sprint duration: 2 weeks
- 10 stories assigned and (all) completed
- Daily stand-ups
- Weekly code retrospectives
- Discord for chat and troubleshooting

# Code Summary
![CRUD](https://github.com/serengetijade/Python/blob/main/DjangoGameHoard/GameHoard/readme/GameHoardCRUD.gif)

## Index Page
The [index (home) page](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_index.html) is where users can create a database record for a game in their collection, access a link to another page to edit it, view records in the WishList DB, view rendered beautifulsoup content, and view rendered API content. 
It is where several functions come together. These CRUD functions have been abstracted, so the user experiences everything seamlessly on (almost) one page. 
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/templates/GameHoard/GH_index.html#L6-L81
- CREATE function is accessed via an included modal from: [GH_create.html](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_create.html) (see modal instructions in [gameHoard.js](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/static/js/gameHoard.js)). The function must be included as part of this view, since here is where the CREATE function is actually performed (by being included, the modal is part of this page).
- READ function in this view accesses the model manager and returns all records from the Game model manager and the WishList model manager, defined in [models.py](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/models.py). Each record in the Game database is iterated into the html template [GH_read.html](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_read.html), where it is parsed as as_p and as as_table. Each record from the WishList database is iterated into the html template [GH_read_wishlist.html](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_read_wishlist.html) by using a django for loop tag.
- Beautifulsoup web scraping is rendered by calling the create_soup function and passing its content in via a variable.
- API content is passed in from the api and apiQuery functions.

https://github.com/serengetijade/Python/blob/162d12b282ae3ee1695448d074b881d6e9371462/DjangoGameHoard/GameHoard/views.py#L34-L69

## Models
Two databases [models](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/models.py) were created for this project: 
- Game databaste: create a record from form inputs that the user fills out and submits. This is a database of games in the user's collection. 
- WishList database: populate a form for each beautifulsoup and API result, and then create or delete a record by clicking 'favorite' button.

https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/models.py#L3-L41

## Create Form ~ Game database
The [game form](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/forms.py) takes user input from a form (via [GH_create.html](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_create.html)) and saves it to the Game database.
It is accessed by clicking on an element (button) in [GH_index.html](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_index.html).
By using the django include tag, it's like this content is part of the [GH_index.html](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_index.html) document.
Therefore, the form and the function to create a record, is defined as part of the GH_index function in [views.py](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/views.py).
JavaScript is used to show and hide this element as a modal pop up, see  [gameHoard.js](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/static/js/gameHoard.js).

https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/templates/GameHoard/GH_create.html#L12-L23


## Create Form ~ WishList database
The [wishlist form](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/forms.py) is included as [GH_create_wishlist.html](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_create_wishlist.html) in the html code of the beautifulsoup and API results.
It is triggered by "action = a django url tag", 
an attribute within the html form tag, which points to a 'shortcut' in [urls.py](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/urls.py), 
which points to a function (create_wishlist) in [views.py](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/views.py).
By using the django include tag, it's like this content is part of the parent document.
And because it's being included INSIDE an iteration loop (in [GH_read_soup](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_read_soup.html) and [GH_read_api](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_read_api.html)) it can access the django tags with each iteration's specific info.
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/templates/GameHoard/GH_read_soup.html#L2-L16

As each result is read and rendered as content, a form is generated as well. The wishlist content is 'triggered' by clicking the submit element. 
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/templates/GameHoard/GH_create_wishlist.html#L9-L15

The inputs of each form is then called by the create_wishlist function, and used to create a record when the 'favorite' button is triggered. 

To put it another way, when 'favorited', that item passes along its own details in a form and uses them to create a record by calling a url/view function. The form is abstracted (hidden by CSS), so all the user has to do is click the 'favorite' icon.
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/views.py#L219-L232

## Read
To read and display the Game and WishList databases, all records are called via each model manager. 
A template is used in each case to add styling to each record. 
For the Game database, records are also rendered as a table, 
which is a modal the user can hide or display by the click of a button (toggled with JavaScript), see  [gameHoard.js](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/static/js/gameHoard.js).
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/templates/GameHoard/GH_read.html#L1-L62

## Update and Delete ~ Game database
The [update page](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_update.html) 
is accessed by clicking on an element (anchor) in another document ([GH_read.html](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_read.html)). 
'UpdateGame' is a 'shortcut' defined in [urls.py](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/urls.py), 
which points the way to a function in [views.py](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/views.py)
named 'updateGameDB', which passes in the primary key from the element that was initially clicked.
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/templates/GameHoard/GH_update.html#L11-L21

The [delete form](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/templates/GameHoard/GH_delete.html) is included in the update page as a modal popup, see  [gameHoard.js](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/static/js/gameHoard.js).
Because it is included, it recieves the primary key the same way the update page does.
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/templates/GameHoard/GH_delete.html#L9-L20

Confirming 'DELETE' in the modal popup submits the form and deletes the record. 
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/views.py#L76-L97

## Delete ~ WishList database
When each WishList record is read and rendered from the database, a form is created using each record's primary key and it is assigned an action that will call the delete_wishlist function in [views.py](https://github.com/serengetijade/tree/main/DjangoGameHoard/GameHoard/blob/main/views.py).
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/templates/GameHoard/GH_read_wishlist.html#L3-L19

https://github.com/serengetijade/Python/blob/291c7d52b0fa774df14bd8f3e7248e604a37f7c0/DjangoGameHoard/GameHoard/views.py#L235-L240

## BeautifulSoup Web Scraping
BeautifulSoup source content credit: [BoardGameQuest](https://www.boardgamequest.com/category/game-reviews/)

![bsoup Display](https://github.com/serengetijade/Python/blob/main/DjangoGameHoard/GameHoard/readme/soup1.jpg)

To provide dynamic content on the page, beautifulsoup was used to scrape a popular board game review page. The results of the list were iterated through and rendered as html objects. 
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/views.py#L115-L141

## API Requests
API source content credit:  [CheapShark](https://apidocs.cheapshark.com/#c33f57dd-3bb3-3b1f-c454-08cab413a115)

![API Display](https://github.com/serengetijade/Python/blob/main/DjangoGameHoard/GameHoard/readme/api1.jpg)
Another source for dynamic content is by using an application programming interface to request data from a website. The returned request was parsed into a dictionary, which was then iterated through and rendered as html objects. 
https://github.com/serengetijade/Python/blob/7e2d5f7e8109f7938026b49a4f443db4614ee7a2/DjangoGameHoard/GameHoard/views.py#L115-L141

![Favorite](https://github.com/serengetijade/Python/blob/main/DjangoGameHoard/GameHoard/readme/favoriteAPI.gif)

## Download Instructions
<details><summary>Requirements</summary>

|Package             |Version       |
|-------------------:|--------------|
|beautifulsoup4      |4.8.0         |
|certifi             |2022.9.24     |
|chardet             |3.0.4         |
|Django              |2.2.5         |
|django-bootstrap4   |1.1.1         |
|django-crispy-forms |1.7.2         |
|djangorestframework |3.11.0        |
|idna                |2.8           |
|pip                 |22.2.2        |
|pytz                |2022.5        |
|requests            |2.22.0        |
|setuptools          |65.4.1        |
|soupsieve           |2.3.2.post1   |
|sqlparse            |0.4.3         |
|urllib3             |1.25.11       |
|wheel               |0.37.1        |

</details>
If you would like to see the app in action for yourself, the repository is ready to download as a complete django app. Note that the readme file included only contains content for this readme, and is not necessary for the app to run.
To download, ensure the required packages are installed then add this repository to your project file. 

1- In the project's <b>settings.py</b> file, include the following: 

INSTALLED_APPS = [ ‘GameHoard’, 

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

STATIC_URL = '/static/'

STATICFILES_DIRS = [
os.path.join(BASE_DIR, "static"),
'/var/www/static',
]

2- In the project's <b>urls.py</b> file, include the following: 

from django.urls import include

urlpatterns = [
    path('GameHoard/', include('GameHoard.urls')),
]

3- In the project's <b>views.py</b> file, include the following:

from django.shortcuts import render

def gameHoard(request):
   return render(request, 'GameHoard/GH_index.html')

4- In the terminal, make migrations to create the database tables

5- Runserver and enjoy

## Source Credits
- Web scraping for board game reviews: [BoardGameQuest](https://www.boardgamequest.com/category/game-reviews/)
- API credit for video game prices: [CheapShark](https://apidocs.cheapshark.com/#c33f57dd-3bb3-3b1f-c454-08cab413a115)

>"Python is an experiment in how much freedom programmers need. Too much freedom and nobody can read another's code; too little and expressiveness is endangered."
–Guido van Rossum