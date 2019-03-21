from rest_framework import serializers
from .models import Todoapp

class TodoappSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'check',
        )
        model = Todoapp
