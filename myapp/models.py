from django.db import models

# Create your models here.

class TodoItem(models.Model):
    # this is the model
    # below is the different fields of the model which is also known as python attributes
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

# register this model to the admin panel
# go to admin.py, the file in which we can register different models


