from django.shortcuts import render
from rest_framework import generics
from .serializer import serial
from .models import Room
# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset=Room.objects.all()
    serializer_class=serial

def index(request):
    return render(request,'index.html')
