from django.contrib import admin
from .models import Seller, Customer, Item, Order
# Register your models here.

admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)