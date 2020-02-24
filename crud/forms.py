from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
      class Meta:
        model = Employee
        fields = ['eid','ename','econtact','eemail','econtact']  #all fields of models to make field in form

