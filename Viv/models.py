from django.db import models

# Create your models here.

class user:
    name : str
    uid : str
    phone : str
    password : str
    mail : str

class category:
    image : str
    text : str
    next : str