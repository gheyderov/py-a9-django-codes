from django.urls import path
from product.api.views import CategoryApiView, TagApiView, product_update, ProductListApiView, ProductRetrieveUpdateView, SubscriberCreateAPIView

urlpatterns = [
    path('categories/', CategoryApiView.as_view(), name = 'categories'),
    path('tags/', TagApiView.as_view(), name = 'tags'),
    path('products/', ProductListApiView.as_view(), name = 'products'),
    path('product/<int:pk>/', ProductRetrieveUpdateView.as_view(), name = 'product_update'),
    path('subscriber/', SubscriberCreateAPIView.as_view(), name = 'subscriber')
]