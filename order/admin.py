from django.contrib import admin
from .models import Wishlist, Basket, BasketItem, Order

# Register your models here.

admin.site.register(Wishlist)
admin.site.register(BasketItem)
admin.site.register(Basket)
admin.site.register(Order)