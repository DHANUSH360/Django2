from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import CloudTable
from .serializers import CloudTableSerializer
from django.views.decorators.csrf import csrf_exempt
import cloudinary

def welcome(req):
    return HttpResponse("Welcome to Dhanush app from render")

def sample(req):
    return JsonResponse({"msg":"json response from render"})

@csrf_exempt
def reg_user(request):
    if request.method == "POST":
        try: 
            user_id=request.POST.get("id")
            user_name=request.POST.get("name")
            user_email=request.POST.get("email")
            user_mob=request.POST.get("mob")
            user_image=request.FILES.get("profile")
            img_url=cloudinary.uploader.upload(user_image)
            print(img_url["secure_url"])

            new_user=CloudTable.objects.create(id=user_id,email=user_email,name=user_name,mob=user_mob,profile_pic=img_url["secure_url"])
            
            return JsonResponse({"msg": "User created successfully!","details":list(new_user.values())})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Only POST method allowed"}, status=405)