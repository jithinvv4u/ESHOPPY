from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/',details,name="details"),
    path('addtocart/<id>',addCart,name='store_cart')
]
