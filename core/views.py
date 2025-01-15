from django.shortcuts import render
from product.models import ProductCategory

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')