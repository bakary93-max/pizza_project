from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.
# Les pizzas: Végétarienne,Cannibale,4 Fromages,Carnivore
def index(request):
    """pizzas = Pizza.objects.all()
    pizzas_names_and_price = [pizza.nom + ": " + str(pizza.prix) + " euros" for pizza in pizzas]
    pizzas_name_and_price_str = ",".join(pizzas_names_and_price)
    return HttpResponse("Les pizzas: " + pizzas_name_and_price_str)
"""
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, "menu/index.html",{'pizzas':pizzas})