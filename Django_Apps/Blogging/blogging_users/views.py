from django.http import HttpResponse
from django.shortcuts import render



def register(request):
    return render(request,"register.html")

def index(request):
    return render(request,"Index.html")
    #return HttpResponse(request,"<h1>Welcome Users</h1>")

