from django.shortcuts import render
from .models import Post

# def index(request):
#     posts = Post.objects.all()
#     return render(request,"Index.html",{"posts":posts})



def postdetails(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,"postdetails.html",{"post":post})
