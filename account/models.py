from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import AbstractModel
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    ips = ArrayField(models.GenericIPAddressField(), null=True, blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        return '/static/images/no-photo.webp'

class UserAddress(AbstractModel):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.address}'
    

class BlockedIps(AbstractModel):
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.ip