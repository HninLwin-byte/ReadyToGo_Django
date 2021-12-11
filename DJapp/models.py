from django.db import models

# Create your models here.
class feature(models.Model):
    name = models.CharField(max_length=100)
    detail= models.CharField(max_length=500)
    
class restaurant(models.Model):
   
    shop = models.CharField(max_length=100)
    about = models.CharField(max_length=1000)

class image(models.Model):
    shop = models.CharField(max_length=100,null=True)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.shop
    

