from django import forms
from .models import Application, Job

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume', 'cover']
        widgets = {
            'cover': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'experience_needed', 'salary', 'description', 'last_date']
        widgets = {
            'last_date': forms.DateInput(format='%d-%m-%Y', attrs={
                'type': 'date',
            })
        }