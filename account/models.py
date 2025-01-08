from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import AbstractModel

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=200, null=True, blank=True)


class UserAddress(AbstractModel):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.address}'