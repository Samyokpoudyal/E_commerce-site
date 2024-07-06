from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    category =models.CharField(max_length=20,default="Not Known")
    sub_category=models.CharField(max_length=20, blank=True)
    prod_name=models.CharField(max_length=20,default="default ")
    Description=models.CharField(max_length=1000,default="default ")
    price=models.IntegerField(default=0)
    img=models.ImageField(upload_to='media',default='Not available')
    discount=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.prod_name
    

class Contact(models.Model):
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=70,default='')
    phone=models.CharField(max_length=11,default='')
    description=models.TextField(max_length=150,default='')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('complain')
    

class Add(models.Model):
    category =models.CharField(max_length=20,default="Not Known")
    sub_category=models.CharField(max_length=20, blank=True)
    prod_name=models.CharField(max_length=20,default="default")
    Description=models.CharField(max_length=1000,default="default")
    price=models.IntegerField(default=0)
    img=models.ImageField(upload_to='media',default='Not available')
    discount=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.prod_name    
    

class Orders(models.Model):
    name=models.CharField(max_length=20)
    caddress=models.CharField(max_length=20)
    maddress=models.CharField(max_length=20)
    quantity=models.IntegerField(default=0)
    email= models.EmailField(max_length = 254)
    phone=models.CharField(max_length=12)
    product_name=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("success", kwargs={"pk": self.pk})
    