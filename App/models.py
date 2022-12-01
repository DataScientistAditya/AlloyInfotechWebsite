from django.db import models
# Create your models here.

#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#pip install django-phonenumber-field[phonenumbers]
class Conctact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Meeseges = models.CharField(max_length=800)