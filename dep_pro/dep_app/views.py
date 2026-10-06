from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import CloudTable
from .serializers import CloudTableSerializer
from django.views.decorators.csrf import csrf_exempt

def welcome(req):
    return HttpResponse("Welcome to Dhanush app from render")

def sample(req):
    return JsonResponse({"msg":"json response from render"})

@csrf_exempt
def reg_user(req):
    user_Data=json.loads(req.body)
    new_user=CloudTable.objects.create(name=user_Data["name"],email=user_Data["email"],mobile=user_Data["mobile"])
    return JsonResponse({"msg":"user created successfully"})