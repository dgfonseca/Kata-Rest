from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Image
import json
from django.contrib.auth import authenticate, login


# Create your views here.
@csrf_exempt
def index(request):
    images_list = Image.objects.all()
    return HttpResponse(serializers.serialize("json", images_list))

@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))

@csrf_exempt
def get_user_image(request, params):
    images_list = Image.objects.filter(user=params)
    return HttpResponse(serializers.serialize("json", images_list))


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user =  authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            message = "Ok"
        else:
            message = "Nombre de usuario o contrasena incorrecto"
    return JsonResponse({"message":message})

def put_user(request, params):
    if request.method == 'PUT':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.get(username=params)
        user_model.username = username
        user_model.password = password
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))



