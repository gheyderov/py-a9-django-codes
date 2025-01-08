from django.db import models
from product.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Wishlist(AbstractModel):
    user = models.ForeignKey(User, related_name='wishlists', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', related_name='wishlists', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class BasketItem(AbstractModel):
    product = models.ForeignKey('product.Product', related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} * {self.quantity}'
    
    def item_price(self):
        return self.product.price * self.quantity
    

class Basket(AbstractModel):
    user = models.ForeignKey(User, related_name='baskets', on_delete=models.CASCADE)
    items = models.ManyToManyField(BasketItem, related_name='baskets')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
    def total_price(self):
        price = 0
        items = self.items.all()
        for item in items:
            price += item.item_price()
        return price
    

class Order(AbstractModel):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, related_name='orders', on_delete=models.CASCADE)
    address = models.ForeignKey('account.UserAddress', related_name='orders', on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=0)

    def __str__(self):
        return self.user.username
    

