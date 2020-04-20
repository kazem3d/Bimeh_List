
from django import forms 
# from django.forms import ModelForm
from main.models import WorkHouse,Workers,MonthList,DetailsList


class WorkhouseForm(forms.ModelForm):
    class Meta:
        model=WorkHouse

        # fields=['Name']
        exclude=[]

class WorkersForm(forms.ModelForm):
    class Meta:
        model=Workers
        exclude=[]

class MonthlistForm(forms.ModelForm):
    class Meta:
        model=MonthList
        exclude=[]

class DetailsForm(forms.ModelForm):
    class Meta:
        model=DetailsList
        exclude=[]