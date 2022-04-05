from django.http import HttpResponse
from django.shortcuts import render
from .serializers import OptionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Table



    # add permission to check if user is authenticated

@api_view(['GET'])
def getdata(request):
    donnee = Table.objects.all()
    serializer = OptionSerializer(donnee, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postd(request):
    donnee = OptionSerializer(data = request.data)
    if donnee.is_valid():
        donnee.save()
    return Response(donnee.data)
# def api_home(request):
#     objet = Table.objects.all()
#     json = serializers.serialize("json", objet)
#     return HttpResponse(json)
# Create your views here.
