from django.urls import path
from core.views import homepage, about, ContactView, export

urlpatterns = [
    path('', homepage, name='home'),
    path('export/', export, name='export'),
    path('about/', about, name = 'about'),
    path('contact/', ContactView.as_view(), name = 'contact'),
]