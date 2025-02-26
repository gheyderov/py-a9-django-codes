from django.urls import path
from product.api.views import categories, products, product_update, ProductListApiView, ProductRetrieveUpdateView


urlpatterns = [
    path('categories/', categories, name = 'categories'),
    path('products/', ProductListApiView.as_view(), name = 'products'),
    path('product/<int:pk>/', ProductRetrieveUpdateView.as_view(), name = 'product_update')
]