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
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('Viv.urls')),
    path('desserts/desserts.html', include('Viv.urls')),
    path('appetizers/appetizers.html', include('Viv.urls')),
    path('specialThali/specialThali.html', include('Viv.urls')),
    path('index/welcome.html', include('Viv.urls')),
    path('signin/signin.html', include('Viv.urls')),
    path('signup/signup.html', include('Viv.urls')),
    path('lunch/lunch.html', include('Viv.urls')),
    path('breakfast/breakfast.html', include('Viv.urls')),
    path('Dinner/dinner.html', include('Viv.urls')),
    path('Cart/cart.html', include('Viv.urls')),
    path('Help/help.html', include('Viv.urls')),
    path('admin/', admin.site.urls),
]
