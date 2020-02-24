from django.shortcuts import render

# Create your views here.

def Dashboard( request):
    test = 'test'
    return render(request, 'index.html')

