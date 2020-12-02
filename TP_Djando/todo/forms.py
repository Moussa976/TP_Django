from django import forms  
from todo.models import Task  
class TaskForm(forms.ModelForm):  
    class Meta:  
        model = Task  
        fields = ['content', 'is_done', 'created_date'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'is_done': forms.CheckboxInput(attrs={ 'class': 'form-control' }),
            'created_date': forms.DateTimeInput(attrs={ 'class': 'form-control' }),
      }