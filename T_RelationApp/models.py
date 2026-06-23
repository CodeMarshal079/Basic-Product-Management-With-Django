from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    USER_TYPE=[
        ('admin', 'Admin'),
        ('customer', 'Customer')
    ]
    user_type =models.CharField(max_length=200, choices=USER_TYPE, null=True)

    def __str__(self):
        return self.username
    
class CategoryModel(models.Model):
    name =models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
    
class ProductModel(models.Model):
    name =models.CharField(max_length=200, null=True)
    price =models.IntegerField(null=True)
    category =models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    description =models.TextField(null=True)
    image =models.ImageField(upload_to='products', null=True)
        
    def __str__(self):
        return self.name
        
class OrderModel(models.Model):
    STATUS=[
        ('pending','Pending'),
        ('in process','In process'),
        ('deleverd','Deleverd')
    ]
    
    user =models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    product =models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    quantity =models.IntegerField(null=True)
    status =models.CharField(max_length=200, choices=STATUS, null=True)
    total =models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.product} Order By {self.user}"
    