from django.contrib import admin
from .models import ProductCategory, Product, ProductImage, ProductTag, ProductReview

# Register your models here.

admin.site.register(ProductCategory)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductReviewInline(admin.TabularInline):
    model = ProductReview


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price', 'get_tags']
    list_display_links = ['title']
    list_editable = ('category',)
    list_filter = ('price', 'category')
    search_fields = ('title', 'category__title')
    inlines = [ProductImageInline, ProductReviewInline]

    def get_tags(self, obj):
        tags = []
        for tag in obj.tags.all():
            tags.append(tag.title)
        return tags


admin.site.register(ProductTag)

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'message', 'is_verified']
    actions = ['update_status']

    def update_status(self, request, queryset):
        queryset.update(is_verified = True)