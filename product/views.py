from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from product.models import Product, ProductCategory, ProductReview
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from product.forms import ProductReviewForm



# Create your views here.

class ShopListView(ListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


# def shop(request):
#     products = Product.objects.all()
#     categories = ProductCategory.objects.all()
#     context = {
#         'products' : products,
#         'categories' : categories
#     }
#     return render(request, 'shop.html', context)


class ShopDetailView(FormMixin, DetailView):
    template_name = 'shop-detail.html'
    model = Product
    form_class = ProductReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ProductReview.objects.filter(product = self.get_object(), is_verified = True)
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            review = form.save(False)
            review.is_verified = False
            review.product = self.object
            review.user = self.request.user
            form.save()
            return redirect(reverse_lazy('shop_detail', kwargs = {'pk' : self.object.id}))
            


# def shop_detail(request, pk):
#     product = get_object_or_404(Product, id = pk)
#     context = {
#         'product' : product
#     }
#     return render(request, 'shop-detail.html', context)