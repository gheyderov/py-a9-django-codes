from django.template import Library
register = Library()
from product.models import ProductCategory


@register.simple_tag
def get_categories(limit = 5):
    return ProductCategory.objects.order_by('-created_at')[:limit]


@register.filter
def capitalize_value(value):
    return value.capitalize()




