from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from posts.models import Post


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            # check mail is exists or not?
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already used.")
                return redirect("register")
            elif User.objects.filter(username = username).exists():
                messages.info(request,"User name already used.")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"Confirm Password is not same.")
    else:
        return render(request,"register.html")




def index(request):
    posts = Post.objects.all()
    posts = posts.order_by("created_at")
    return render(request,"Index.html",{"posts":posts})
    #return HttpResponse(request,"<h1>Welcome Users</h1>")





def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Credientials Invalid.")
            return redirect("login")

    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect("login")





def posts(request,pk):
    return render(request,"post.html",{"pk":pk})



