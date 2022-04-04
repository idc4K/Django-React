from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Table

# def api_home(request):
#     objet = Table.objects.all()
#     json = serializers.serialize("json", objet)
#     return HttpResponse(json)
# Create your views here.
