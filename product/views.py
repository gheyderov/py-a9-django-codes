from django.shortcuts import render, get_object_or_404
from product.models import Product, ProductCategory

# Create your views here.

def shop(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'products' : products,
        'categories' : categories
    }
    return render(request, 'shop.html', context)


def shop_detail(request, pk):
    product = get_object_or_404(Product, id = pk)
    context = {
        'product' : product
    }
    return render(request, 'shop-detail.html', context)