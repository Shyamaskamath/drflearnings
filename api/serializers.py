from rest_framework import serializers
from .models import Todolist

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ['id', 'title', 'description', 'create_at', 'update_at', 'completed']

