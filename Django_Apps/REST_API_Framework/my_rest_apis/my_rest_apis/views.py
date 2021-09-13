from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser

from rest_framework.response import Response
from drf_app.serializers import StudentSerializer
from drf_app.models import Student

class TestView(APIView):

    permission_classes = (IsAuthenticated,)
    #permission_classes = ()

    def get(self,request,*args,**kwargs):
        # data = {"username":"admin",
        # "no_of_years_active":10
        # }
        qs = Student.objects.all()
        serializer = StudentSerializer(qs,many=True)

        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



