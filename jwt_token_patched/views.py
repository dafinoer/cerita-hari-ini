from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
from .serializer import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
