from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class watches(models.Model):
   name=models.CharField(max_length=100)
   description=models.TextField()
   price=models.FloatField()
   updated=models.DateTimeField(auto_now=True)
   created=models.DateTimeField(auto_now_add=True)



class watchUploads(models.Model):
   name=models.CharField(max_length=100)
   description=models.TextField()
   price=models.FloatField()
   image=models.ImageField(upload_to='watch_images/')
   updated=models.DateTimeField(auto_now=True)
   created=models.DateTimeField(auto_now_add=True)


class wishlist(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)  
   product=models.ManyToManyField(watchUploads) 
   updated=models.DateTimeField(auto_now=True)
   created=models.DateTimeField(auto_now_add=True)


class cart(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)  
   product=models.ManyToManyField(watchUploads) 
   updated=models.DateTimeField(auto_now=True)
   created=models.DateTimeField(auto_now_add=True)



class CartItem(models.Model):   
    user = models.ForeignKey(cart, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(watchUploads, on_delete=models.CASCADE)
    cart_count = models.IntegerField(default=1)