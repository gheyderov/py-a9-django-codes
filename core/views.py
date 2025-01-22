from django.shortcuts import render, redirect
from core.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        print('post')
        form = ContactForm(data=request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            messages.add_message(request, messages.SUCCESS, "Successfully Sent!")
            return redirect(reverse_lazy('contact'))
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)