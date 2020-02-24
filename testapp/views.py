
from django.shortcuts import render
from .forms import ContactForm, ContactModelForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form1': form})

def snipt_form(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactModelForm()
    return render(request, 'home.html', {'form': form})

