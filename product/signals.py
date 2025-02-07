from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from django.utils.text import slugify

@receiver(post_save, sender=Product)
def product_slug(instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title) + str(instance.id)
        instance.save()