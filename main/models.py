from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.email
    

class Item(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='item')
    title = models.CharField(max_length=150)
    available_units = models.IntegerField()

    def __str__(self):
        return self.title
    
    def decrease_units(self, quantity):
        if self.available_units >= quantity:
            self.available_units -= quantity
            self.save()
            return True
        return False

class Customer(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=250)
    address = models.TextField() 
    phone_num = models.CharField(max_length=20)
  
    def __str__(self):
        return self.name
    
class Order(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='order')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    