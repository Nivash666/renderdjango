from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class Home(APIView):
    def get(self,request):
        msg="hello world"
        return Response({'msg':msg})