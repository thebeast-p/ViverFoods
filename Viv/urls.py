"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.welc,name="Welcome"),
    path('index/welcome.html', views.welc,name="Welcome"),
    path('signin/signin.html', views.signin, name='SignIn'),
    path('signin.html', views.signin, name='SignIn'),
    path('signup/signup.html', views.signup, name='SignUp'),
    path('breakfast/breakfast.html',views.breakfast, name='Breakfast'),
    path('lunch/lunch.html', views.lunch,name="Lunch"),
    path('desserts/desserts.html', views.desserts,name="Desserts"),
    path('appetizers/appetizers.html', views.appetizer,name="Appetizers"),
    path('specialThali/specialThali.html', views.specialThali,name="Special Thali"),
    path('Dinner/dinner.html', views.dinner,name="Dinner"),
    path('Help/help.html', views.help,name="FAQs"),
    path('Cart/cart.html', views.cart,name="Cart")
]
