from django.db import models
from blog.models import AbstractModel
from core.validators import validate_gmail

# Create your models here.


class Subscriber(AbstractModel):
    email = models.EmailField('email', unique=True)

    def __str__(self):
        return self.email


class Contact(AbstractModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.first_name