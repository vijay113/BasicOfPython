from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        res = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ city+"&appid=e3c337530c2f1db6f8c177c6eeb57d7b").read()
        json_data = json.loads(res)
        weather= list( json_data["weather"])
        main_obj= weather[0]
        data= {
            "city":city,
            "weather": str(main_obj["main"]) +"; "+str(main_obj["description"]),
            "country": str(json_data['sys']['country']),
            "coordinate":str(json_data["coord"]["lon"])+" "+str(json_data["coord"]["lat"]),
            "temp":str(json_data["main"]["temp"])+ "K",
            "pressure":str(json_data["main"]["pressure"]),
            "humidity":str(json_data["main"]["humidity"]),
            "wind":str(json_data["wind"]["speed"])+ "m/s"
        }
    else:
        city = ""
        data = {}
    return render(request,"index.html",{"data":data})



