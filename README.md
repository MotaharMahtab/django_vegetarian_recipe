# django_vegetarian_recipe

## <a href='https://youtu.be/6jMvJNuxIsg'>Project Demo Video</a> 
![Alt text](https://github.com/MotaharMahtab/django_vegetarian_recipe/blob/main/Functionalities.gif)

## Project Description
This web app allows users to view different vegetarian recipes, see their total calories, nutrients like protein, carbohydrate, fat and their ingredients. It also allows users to order the recipes although payment option is not implemented yet. Recipes have categories and tags which will allow users to choose among different categories and tags.

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv envname
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
