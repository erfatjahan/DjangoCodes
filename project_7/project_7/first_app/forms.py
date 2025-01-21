from django import forms
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        labels={
            'name':'student Name',
            'roll':'student Roll'
        }
        widgets = {
      'name': forms.TextInput(attrs={'class': 'btn-primary', 'placeholder': 'Enter your name'}),
    #   'roll':forms.PasswordInput()
    }
    help_texts={
        'name':"write your full name"
   }
    error_messages={
        'name':{'required':"your name is required"}
    }