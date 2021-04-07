python manage.py startapp myapp
 
python manage.py migrate 

python manage.py makemigrations myapp

python manage.py sqlmigrate myapp 0001

python manage.py migrate myapp     

 python manage.py createsuperuser


This will create another directory called hello_world with several files:

__init__.py tells Python to treat the directory as a Python package.
admin.py contains settings for the Django admin pages.
apps.py contains settings for the application configuration.
models.py contains a series of classes that Django’s ORM converts to database tables.
tests.py contains test classes.
views.py contains functions and classes that handle what data is displayed in the HTML templates.


python manage.py startapp projects
