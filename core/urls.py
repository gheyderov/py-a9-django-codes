from django.urls import path
from core.views import homepage, about

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about, name = 'about')
]