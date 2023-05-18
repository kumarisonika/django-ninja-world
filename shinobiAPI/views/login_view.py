# views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
import uuid, hashlib
from rest_framework import status
from shinobiAPI.serializers import UserSerializer



@api_view(['POST'])
def sign_up(request):
    if request.method == 'POST':
        user_data= JSONParser().parse(request)
        user_object={}
        user_object['username']=user_data["username"]
        salt=uuid.uuid4().bytes
        user_object['salt']=salt
        hash_password=hashlib.sha256(user_data["password"].encode()+salt).digest()
        user_object['hashed_password']=hash_password
        user_serilizer= UserSerializer(data=user_object)
        if user_serilizer.is_valid():
            user_serilizer.save()
            return JsonResponse(user_serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(user_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
       
          
@api_view(['POST'])
def log_in(request):
    if request.method == 'POST':
        user_data= JSONParser().parse(request)
        salt=b'\xe635o<eD{\xabH\xbakyV\xe2\x1d'
        hash_password=hashlib.sha256(user_data["password"].encode()+salt).digest()
        if hash_password == b'3B.[\x8f\x9c\x8b]H\x1e\xa3(\xd0u\xfd\x9b\xd4=\xea\x0e\x84V~\x89\x98.O\xb9\xad\x15u\xae':
            return JsonResponse({"status":True,"message":"Login Successful"})
        else:
            return JsonResponse({"status":False,"message":"Login Failed"}, status=status.HTTP_403_FORBIDDEN)

# b'\xe635o<eD{\xabH\xbakyV\xe2\x1d' b'3B.[\x8f\x9c\x8b]H\x1e\xa3(\xd0u\xfd\x9b\xd4=\xea\x0e\x84V~\x89\x98.O\xb9\xad\x15u\xae'