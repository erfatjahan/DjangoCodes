from django.shortcuts import render
from first_app.forms import StudentForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()  
            print(form.cleaned_data)  
            
    else:
        form = StudentForm() 

    return render(request, 'home.html', {'form': form})