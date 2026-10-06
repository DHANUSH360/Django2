from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def welcome(req):
    return HttpResponse("Welcome to Dhanush app from render")
