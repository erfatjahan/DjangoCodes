from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author':'erfat','age' :20,'list':['python','is','best'],'courses':[

{
    'id':1,
    'name':'python',
    'fee':100,
},
{
    'id':2,
    'name':'django',
    'fee':500,
},
{
    'id':3,
    'name':'c++',
    'fee':5000,
},
    ]}
    return render(request,'home.html',d)