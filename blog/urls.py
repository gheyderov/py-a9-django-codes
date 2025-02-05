from django.urls import path
from blog.views import blogs, BlogCreateView

urlpatterns = [
    path('blogs/', blogs, name='blogs'),
    path('blog-create/', BlogCreateView.as_view(), name='create_blogs')
]