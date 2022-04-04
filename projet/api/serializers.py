from rest_framework import serializers
from .models import Table
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ["nom", "prenom"]