from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

cat1= category()
cat1.image = 'breakfast.jpg'
cat1.text = 'Breakfast'
cat1.next = "../breakfast/breakfast.html"

cat2= category()
cat2.image = 'lunch.jpg'
cat2.text = 'Lunch'
cat2.next = "../lunch/lunch.html"

cat3= category()
cat3.image = 'dinner.jpg'
cat3.text = 'Dinner'
cat3.next = "../Dinner/dinner.html"

cat4= category()
cat4.image = 'special_thali.jpg'
cat4.text = 'Special Thali'
cat4.next = "../specialThali/specialThali.html"

cat5= category()
cat5.image = 'ice_cream.jpg'
cat5.text = 'Snacks'
cat5.next = "../desserts/desserts.html"

cat6= category()
cat6.image = 'coke.jpg'
cat6.text = 'Appetizers'
cat6.next = "../Appetizers/Appetizers.html"

cats = [cat1, cat2, cat3, cat4, cat5, cat6]

def welc(request):
    return render(request, 'welcome.html', {'cats':cats})


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')


def lunch(request):
    return render(request, 'lunch.html')


def breakfast(request):
    return render(request, 'breakfast.html')


def dinner(request):
    return render(request, 'dinner.html')


def appetizer(request):
    return render(request, 'appetizers.html')


def specialThali(request):
    return render(request, 'specialThali.html')


def desserts(request):
    return render(request, 'desserts.html')    


def cart(request):
    return render(request, 'cart.html')    


def help(request):
    return render(request, 'help.html')    