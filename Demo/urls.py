"""
URL configuration for Demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myapp.urls")) # name of the application
    # whenever go to the empty string, it is going to forward all the different URLs or roots into "myapp.urls"
    # that be handled here
    # ex. path("myapp/home, include) that path will be handled myapp/urls's file
]
# create url root, that allows us to connect to our application.
# in the DEMO we have all base roots or URLs for our entire project.
# we need to kind of create  a URL here that will link into our specific application.
# this main part will be handled by this main application.


