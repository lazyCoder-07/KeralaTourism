from django.db import models

# Create your models here.
class ktd(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    psw1 = models.CharField(max_length=20)
    psw2 = models.CharField(max_length=20,default='')

class chatinput(models.Model):
    message = models.CharField(max_length=500)


