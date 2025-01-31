from django.shortcuts import render, redirect
from core.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Successfully Sent!")
        return super().form_valid(form)


# def contact(request):
#     form = ContactForm
#     if request.method == 'POST':
#         print('post')
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             print('valid')
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Successfully Sent!")
#             return redirect(reverse_lazy('contact'))
#     context = {
#         'form' : form
#     }
#     return render(request, 'contact.html', context)