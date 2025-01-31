from django.urls import path
from core.views import homepage, about, ContactView

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about, name = 'about'),
    path('contact/', ContactView.as_view(), name = 'contact'),
]