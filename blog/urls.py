from django.urls import path
from blog.views import blogs

urlpatterns = [
    path('blogs/', blogs, name='blogs')
]