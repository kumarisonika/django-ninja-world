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



@api_view(['POST'])
def sign_up(request):
    if request.method == 'POST':
       input_data= JSONParser().parse(request)
       print(input_data["username"],"kjvgdfgvui")
       salt=uuid.uuid4().bytes
       hash_password=hashlib.sha256(input_data["password"].encode()+salt).digest()
       print(salt,hash_password,"kjkjsdghfudsgui")
       return JsonResponse(input_data)
    
@api_view(['POST'])
def log_in(request):
    if request.method == 'POST':
        input_data= JSONParser().parse(request)
        salt=b'\xe635o<eD{\xabH\xbakyV\xe2\x1d'
        hash_password=hashlib.sha256(input_data["password"].encode()+salt).digest()
        if hash_password == b'3B.[\x8f\x9c\x8b]H\x1e\xa3(\xd0u\xfd\x9b\xd4=\xea\x0e\x84V~\x89\x98.O\xb9\xad\x15u\xae':
            return JsonResponse({"status":True,"message":"Login Successful"})
        else:
            return JsonResponse({"status":False,"message":"Login Failed"}, status=status.HTTP_403_FORBIDDEN)

# b'\xe635o<eD{\xabH\xbakyV\xe2\x1d' b'3B.[\x8f\x9c\x8b]H\x1e\xa3(\xd0u\xfd\x9b\xd4=\xea\x0e\x84V~\x89\x98.O\xb9\xad\x15u\xae'