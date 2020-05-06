# we import the path function, and then import the include function so we can
# include some default authentication URLs that django has defined.
from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
]