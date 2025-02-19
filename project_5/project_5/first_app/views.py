from django.shortcuts import render
from . forms import contactForm,StudentData,PasswordValidationProject

# Create your views here.
def home(request):
    return render(request,'first_app/home.html')
def about(request):
    # return render(request,'first_app/about.html')
    if  request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request,'first_app/about.html',{'name':name,'email':email,'select':select})
    else :
     return render(request,'first_app/about.html')
def submit_form(request):
    return render(request,'first_app/form.html')
def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request, 'first_app/django_form.html', {'form': form})
    else:
        form = contactForm()
    return render(request, 'first_app/django_form.html', {'form': form})

from django.shortcuts import render
from .forms import StudentData

def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            # Handle valid form data
            print("Cleaned Data:", form.cleaned_data)
    else:
        form = StudentData()  # For GET requests, initialize an empty form

    # Always return a response
    return render(request, 'first_app/django_form.html', {'form': form})
def PasswordValidationProject(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print("Cleaned Data:", form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(request, 'first_app/django_form.html', {'form': form})
