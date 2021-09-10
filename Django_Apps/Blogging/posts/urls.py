from django.urls import path
from . import views

urlpatterns = [
path("postdetails/<int:pk>",views.postdetails, name = "postdetails")
]


