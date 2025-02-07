from django.urls import path
from product.views import ShopListView, ShopDetailView

urlpatterns = [
    path('shop/', ShopListView.as_view(), name='shop'),
    path('shop/<str:slug>/', ShopDetailView.as_view(), name= 'shop_detail')
]