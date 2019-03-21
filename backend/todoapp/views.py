from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Todoapp
from .serializers import TodoappSerializer


class ListPost(generics.ListCreateAPIView):
    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializer
