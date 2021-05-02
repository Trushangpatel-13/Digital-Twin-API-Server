from rest_framework import serializers
from django.contrib.auth.models import User

class HelloSerializer(serializers.Serializer):

    Username = serializers.EmailField(max_length=254)
    Password = serializers.CharField(max_length=74)



