# created file, so we can place different url and coonect them to our view

from django.urls import path
from . import views
# import views.py file

# a variable, inside specific paths that will connect a url pattern to a specific path or view.
urlpatterns = [
    # empty path, kind of URL of our website.
    path("", views.home, name="home"),
    # going to call views.home function, which will allows us to view http response

    path("todos/", views.todos, name="Todos")

]

