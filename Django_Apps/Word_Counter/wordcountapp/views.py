
from django.http import HttpResponse
from django.shortcuts import render
from .models import MyText

def index(request):
     #return HttpResponse("<h1>Hello</h1>")
     return render(request,"index.html")



def counter(request):
    # words = request.GET["text"]
     words = request.POST["text"]
     count = len(words.split())
     my_text1 = MyText(words,count)
     
     return render(request,"counter.html", {"mytext":my_text1})



