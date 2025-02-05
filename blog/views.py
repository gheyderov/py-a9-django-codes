from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from blog.models import Blog
from django.views.generic import CreateView
from blog.forms import BlogCreateForm


# Create your views here.

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'blog.html', context)


class BlogCreateView(UserPassesTestMixin, CreateView):
    template_name = 'blog-create.html'
    form_class = BlogCreateForm
    success_url = reverse_lazy('blogs')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser