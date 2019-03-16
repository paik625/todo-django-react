from django.shortcuts import render
from rest_framework import generics

from .models import Todoapp
from .serializers import TodoappSerializer

class ListPost(generics.ListCreateAPIView):
    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializer