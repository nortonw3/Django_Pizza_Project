from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Pizza, Topping, Comment
from django.contrib.auth.decorators import login_required


# Create your views here.

# when a URL request matches the pattern we just defined,
# Django looks for a function called index() in the views.py file
def index(request):
    """ The home page """
    return render(request, 'pizzas/index.html')


from .models import Pizza

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    # a context is a dictionary in which the keys are names we'll use
    # in the template to access the data, and the values are the data
    # we need to send to the template. In this case, theres one key-value pair,
    # which contains the set of pizzas we'll display on the page
    context = {'pizzas':pizzas}
    # when building a page that uses dat, we pass the context variable to render()
    # as well as the request object and the path to the template
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    # just like we did in MyShell.py
    pizza = Pizza.objects.get(id=pizza_id)
    # foreign key can be accessed using '_set'
    toppings = pizza.topping_set.order_by('-date_added')
    comments = pizza.comment_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments}

    return render(request, 'pizzas/pizza.html', context)

@login_required
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        # no data submitted; create a blank form (create an instance of CommentForm)
        # Because we included no arguments when initiating CommentForm, Django
        # creates a blank from that the user can fill out
        form = CommentForm()
    else:
        # POST data submitted; process data
        # we make an instance of CommentForm and pass it the data entered by the user,
        # stored in the request.POST
        form = CommentForm(data=request.POST)
        # The is_valid() method checks that all required fields have been filled
        # in (all fields in a form are required by default) and the data entered
        # matches the field types expected
        if form.is_valid():
            # When we call save(), we include the argument commit=False to tell Django to create 
            # a new entry object and assign it to new_comment without saving it to the database
            new_comment = form.save(commit=False)
            # assign the pizza of the new entry based on the pizza we pulled from pizza_id
            new_comment.pizza = pizza
            new_comment.owner = request.user
            # write the data from the form to the database
            form.save()
            # redirect the user's browser to the pizza page
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    # display a blank form using the new_comment.html template
    context = {'form': form, 'pizza': pizza}
    return render(request, 'pizzas/new_comment.html', context)