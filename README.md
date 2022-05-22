# django_vegetarian_recipe

## <a href='https://youtu.be/6jMvJNuxIsg'>Project Demo Video</a> 
![Alt text](https://github.com/MotaharMahtab/django_vegetarian_recipe/blob/main/Functionalities.gif)

## Project Description
This web app allows users to view different vegetarian recipes, see their total calories, nutrients like protein, carbohydrate, fat and their ingredients. It also allows users to order the recipes although payment option is not implemented yet. Recipes have categories and tags which will allow users to choose among different categories and tags.

Vegetarian Food Recipe project follows the Model-View-Template (MVT) which is slightly different from MVC. It is a collection of three essential components Model, View, and Template. These three layers are responsible for different things, and we use them independently. Django is a popular web development framework that uses the MVT design pattern. 
The main difference between the two patterns is that Django itself takes care of the Controller part (Software Code that controls the interactions between the Model and View), leaving us with the template.

The model helps to handle database. Models help developers to create, read, update, and delete objects (CRUD operations) in the original database. Also, they hold business logic, custom methods, properties, and other things related to data manipulation.

The view is used to execute the business logic and interact with a model to carry data and renders a template. The view fetches data from a model. Then, it either gives each template access to specific data to be displayed, or it processes data beforehand. It accepts HTTP requests, applies business logic provided by Python classes and methods, and provides HTTP responses to the client requests.

The template is a presentation layer that handles the User Interface part completely. These are files with HTML code, which is used to render data. 

For our project, we follow this MVT pattern of Django. Django also takes care of the admin permissions, user permissions and admin view of the app. The Login and signup functionality of the project is directly derived from the following repository: riifaat/TrackYourTask in order to focus on the main project functionality. The test cases for login and sign up functionality are also similar to this repository.

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
.\envname\Scripts\activate
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```
