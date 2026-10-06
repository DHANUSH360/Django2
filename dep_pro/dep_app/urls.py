from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('welcome/', view=views.welcome)

]