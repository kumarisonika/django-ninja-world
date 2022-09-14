from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from shinobiAPI.models import Village
from shinobiAPI.serializers import VillageSerializer
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("Hello! Balle balle!!")

@api_view(['GET', 'POST', 'DELETE'])
def village_list(request):
    # GET list of Villages, POST a new Village, DELETE all Villages
    if request.method == 'GET':
        villages = Village.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            villages = villages.filter(title__icontains=title)
        
        villages_serializer = VillageSerializer(villages, many=True)
        
        return JsonResponse(villages_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        village_data = JSONParser().parse(request)
        village_serializer = VillageSerializer(data=village_data)
        if village_serializer.is_valid():
            village_serializer.save()
            return JsonResponse(village_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(village_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Village.objects.all().delete()
        return JsonResponse({'message': '{} Villages were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'PUT', 'DELETE'])
def village_details(request, pk):
    # find Village by pk (id)
    try: 
        village = Village.objects.get(pk=pk)
    except village.DoesNotExist: 
        return JsonResponse({'message': 'The Village does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        village_serializer = VillageSerializer(village) 
        return JsonResponse(village_serializer.data)
    elif request.method == 'PUT': 
        village_data = JSONParser().parse(request) 
        village_serializer = VillageSerializer(village, data=village_data) 
        if village_serializer.is_valid(): 
            village_serializer.save() 
            return JsonResponse(village_serializer.data) 
        return JsonResponse(village_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        village.delete() 
        return JsonResponse({'message': 'Village was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)