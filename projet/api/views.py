from django.http import HttpResponse
from django.shortcuts import render
from .serializers import OptionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Table



    # add permission to check if user is authenticated

@api_view(['GET'])
def getData(request):
    donnee = Table.objects.all()
    serializer = OptionSerializer(donnee, many=True)
    return Response(serializer.data)   
# def api_home(request):
#     objet = Table.objects.all()
#     json = serializers.serialize("json", objet)
#     return HttpResponse(json)
# Create your views here.
