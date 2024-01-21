from django.contrib import admin
from .models import TodoItem

# Register your models here.

admin.site.register(TodoItem)

# * Any time we make a change to database model, so some migrations
# Migration is some automatic code which django will apply to database which allows you to change the models and update
# them well kind of maintaining the data and ensuring them

# python manage.py makemigrations
# python manage.py migrate

# it updates the database whenever you make the change
# update the migrations and django will automatically update the database it self