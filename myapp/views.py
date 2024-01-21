# return http response
from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.

# created a request object as a parameter which will allow us to access things like query parameter
# and the body of the different request being sent to this function
def home(request):
    # return some response
    #return HttpResponse("Hello world!") # display on the website
    # so we have the view which is simply a function that return some kind of response, we need to actually
    # connect this to our application through a root or a URL.

    return render(request, "home.html")
    # for the render function, we're gonna past request which is home(request), then pass the name of our template

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
    # pass todos dictionary for python
    # create the url for this template go to urls.py in myapp






