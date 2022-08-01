from rest_framework import serializers
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=32)
    dob = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'dob']


class LoginSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=64)

    class Meta:
        model = User
        fields = ['name', 'password']
