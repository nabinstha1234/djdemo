from django.shortcuts import render, redirect
from crud.forms import EmployeeForm
from crud.models import Employee

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    return render(request, 'home.html', {'form': form})

def show(request):
    employee = Employee.objects.all()
    return render(request, 'show.html', {'formshow':employee})



