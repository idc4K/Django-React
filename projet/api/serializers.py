from rest_framework import serializers
from .models import Table
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'