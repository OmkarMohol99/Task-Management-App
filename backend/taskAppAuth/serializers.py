from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class SignupUser(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "password"]


    def create(self, validated_data):
      password = make_password(validated_data.pop("password"))
      user = User(**validated_data, password=password)
      user.save()
      return user
