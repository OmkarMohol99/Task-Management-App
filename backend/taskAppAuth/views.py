from django.shortcuts import render
from rest_framework import generics
from.serializers import SignupUser
from django.contrib.auth.models import User


class SignupUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupUser
