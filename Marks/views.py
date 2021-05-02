from rest_framework.views import APIView
from rest_framework.response import Response
import pyrebase
from . import serializers
from rest_framework import status

from django.http import response,request
from django.shortcuts import render


firebaseConfig = {
    "apiKey": "AIzaSyBrfRUIgZ_5HgN_qynLsl71pGT7CRlE0AM",
    "authDomain": "mgvcl-31954.firebaseapp.com",
    "databaseURL": "https://mgvcl-31954.firebaseio.com",
    "projectId": "mgvcl-31954",
    "storageBucket": "mgvcl-31954.appspot.com",
    "messagingSenderId": "668719767478",
    "appId": "1:668719767478:web:e52e8d14d780a5c031ab17"
  };

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
Dict = {}
class MarksApiView(APIView):
     """Server API View"""
     serializer_class = serializers.HelloSerializer
     def get(self,request,format=None):

         id = self.request.query_params.get('windmill')
         stream = db.child(id).child('DATA').get()
         data = stream.val()
         an_apiview = ['Use Post request for Progress bar']

         return Response(data)
     def post(self,request):
         """Post request"""
         serializers = self.serializer_class(data = request.data)
         if serializers.is_valid():
             message = {}
             Username= serializers.validated_data.get('Username')
             Password = serializers.validated_data.get('Password')
             #message = Scrapy(Username,Password)
             message = {"Hello":"Trushang Patel"}
             return Response(message)
         else:
             return Response(
                 serializers.errors,
                 status=status.HTTP_400_BAD_REQUEST
             )

def index(request):
     return render(request, 'Marks/index.html')

