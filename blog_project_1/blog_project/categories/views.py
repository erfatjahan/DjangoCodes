from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_categories(request):
    if request.method=="POST":
        CategoryForm=forms.CategoryForm(request.POST)
        if CategoryForm.is_valid():
          CategoryForm.save()
          return redirect('add_categories')
    else:
          CategoryForm=forms.CategoryForm()
    return render(request,'add_category.html',{'form':CategoryForm})