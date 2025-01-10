from django.db import models
from blog.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class ProductTag(AbstractModel):

    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class ProductCategory(AbstractModel):

    title = models.CharField(max_length=200, unique=True)
    parent = models.ForeignKey(
        "self",
        related_name="sub_categories",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.parent:
            return f'{self.parent} - {self.title}'
        return self.title

    class Meta:
        verbose_name_plural = "Product Categories"


class Product(AbstractModel):

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        "ProductCategory", related_name="products", on_delete=models.CASCADE
    )
    tags = models.ManyToManyField("ProductTag", blank=True, related_name="products")
    cover_image = models.ImageField(upload_to="product_images/")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


class ProductImage(AbstractModel):
    image = models.ImageField(upload_to="product_images/")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self):
        return self.product.title


class ProductReview(AbstractModel):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    message = models.TextField()
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} | {self.product.title}'