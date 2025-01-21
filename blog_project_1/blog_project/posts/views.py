from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.
def add_posts(request):
    if request.method=="POST":
        PostForm=forms.PostForm(request.POST)
        if PostForm.is_valid():
          PostForm.save()
          return redirect('add_posts')
    else:
          PostForm=forms.PostForm()
    return render(request,'add_post.html',{'form':PostForm})
def edit_posts(request,id):
    post=models.Post.objects.get(pk=id)
    Post_Form=forms.PostForm(instance=post)
#     print(post.title)
    if request.method=="POST":
        Post_Form=forms.PostForm(request.POST,instance=post)
        if Post_Form.is_valid():
          Post_Form.save()
          return redirect('homepage')
    return render(request,'add_post.html',{'form':Post_Form})
def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')