from django.http import HttpResponse
from django.shortcuts import render
from .serializers import OptionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Table



    # add permission to check if user is authenticated

@api_view(['GET'])
def all(request):
	api_urls = {
		'List':'/task-list/',
		'Detail Vue':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)
@api_view(['GET'])
def getdata(request):
    donnee = Table.objects.all()
    serializer = OptionSerializer(donnee, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request, pk):
	donnee = Table.objects.get(id=pk)
	serializer = OptionSerializer(donnee, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    donnee = OptionSerializer(data = request.data)
    if donnee.is_valid():
        donnee.save()
    return Response(donnee.data)

@api_view(['POST'])
def taskupdate(request, pk):
	donnee = Table.objects.get(id=pk)
	serializer = OptionSerializer(instance=donnee, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskdelete(request, pk):
	donnee = Table.objects.get(id=pk)
	donnee.delete()

	return Response('Item succsesfully delete!')
# def api_home(request):
#     objet = Table.objects.all()
#     json = serializers.serialize("json", objet)
#     return HttpResponse(json)
# Create your views here.
