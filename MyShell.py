import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzaria.settings")

import django
django.setup()

from pizzas.models import Pizza

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)


p = Pizza.objects.get(id=3)

print(p.text)
print(p.date_added)

toppings = p.topping_set.all()

for topping in toppings:
    print(topping)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)