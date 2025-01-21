from django import forms
from django.core import validators
class contactForm(forms.Form):
    name=forms.CharField(label='Full name:',
    help_text="total length must be 30 chracters",required=False,widget=forms.Textarea(attrs={'id':'text_area','placeholder':"enter your name"}))
    # file=forms.FileField()
    email=forms.EmailField(label='User Email')
    age=forms.IntegerField(label='User Age')
    weight=forms.FloatField()
    balance=forms.DecimalField()
    check=forms.BooleanField()
    birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appoinment=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES=[('S','small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    meal=[('p','pepperoni'),('M','Mashroom'),('B','Beef')]
    pizz=forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname=self.cleaned_data['name']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10 charecter")
    #     return valname
    # def clean_email(self):
    #     valemail=self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Yout email must contain.com")
    #     return valemail
    # def clean(self):
    #     cleaned_data =super().clean()
    #     valname=self.cleaned_data['name']
    #     valemail=self.cleaned_data['email']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10 charecter")
    #     if '.com' not in valemail:
    #        raise forms.ValidationError("Yout email must contain.com")
class StudentData(forms.Form):
    name=forms.CharField(validators=[validators.MaxLengthValidator(10,message='Enter a name with ai least 10 charecters')])
    email=forms.CharField(widget=forms.EmailInput,)
    age=forms.CharField()
from django import forms

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput, label="Name")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match. Please try again.")

        return cleaned_data
