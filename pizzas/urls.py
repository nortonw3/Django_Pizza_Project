# the path function, which is needed when mapping URLs to views
from django.urls import path

from . import views
# the variable app_name helps Django distinguish this urls.py from
# files of the same name in other apps within the project
app_name = 'pizzas'

# the variable urlpatterns in this module is a list of individual pages
# that can be requested from the pizzas app
urlpatterns = [
    # the first argument is is an empty string '' which matches the
    # base URL - http://localhost:8000. the second argument specifies
    # the function name to call in views.py. the third argument provides
    # the name 'index' for this url pattern to refer to it later
    path('', views.index, name='index'),
    path('pizzas', views.pizzas, name='pizzas'),
    # the integer value is stored in the variable pizza_id and will
    # be subsequently passed to the topic function in views.py
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    path('new_comment/<int:pizza_id>/', views.new_comment, name='new_comment'),
]