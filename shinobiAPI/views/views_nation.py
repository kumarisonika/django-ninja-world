from argparse import _VersionAction
from pstats import Stats
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from shinobiAPI.models import Nation
from shinobiAPI.serializers import NationSerializer
from rest_framework.decorators import api_view



def index(request):
    return HttpResponse("The Nation Table")

@api_view(['GET', 'POST', 'DELETE'])
def nation_list(request):

    if request.method =='GET':
        nations = Nation.objects.all()

        nation_serilizer = NationSerializer(nations, many=True)
        return JsonResponse(nation_serilizer.data, safe=False)
    elif request.method=='POST':
        nation_data =JSONParser().parse(request)
        nation_serializer = NationSerializer(data=nation_data)
        if nation_serializer.is_valid():
            nation_serializer.save()
            return JsonResponse(nation_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(nation_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        count = Nation.objects.all.delete()
        return JsonResponse({'message': '{} All nations are deleted successfully! '.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def nation_details(request,pk):
    try: 
        nation = Nation.objects.get(pk=pk)
    except nation.DoesNotExist:
        return JsonResponse({'message': 'The nation does not exist in the table'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': 
        nation_serializer = NationSerializer(nation) 
        return JsonResponse(nation_serializer.data)
    elif request.method == 'PUT': 
        nation_data = JSONParser().parse(request) 
        nation_serializer = NationSerializer(nation, data=nation_data) 
        if nation_serializer.is_valid(): 
            nation_serializer.save() 
            return JsonResponse(nation_serializer.data) 
        return JsonResponse(nation_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        nation.delete() 
        return JsonResponse({'message': 'Nation was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

