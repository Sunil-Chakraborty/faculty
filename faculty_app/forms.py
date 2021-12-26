from django.forms import ModelForm
from django import forms 
from .models import Faculty

class FacultyForm(forms.ModelForm):  
    class Meta:  
        model = Faculty  
        # fields = "__all__"
        fields = ['username','email','department']
         
        widgets = {
            'email': forms.TextInput(attrs={'size': 40}),            
            'department': forms.CheckboxSelectMultiple(),        
         }
              
                             