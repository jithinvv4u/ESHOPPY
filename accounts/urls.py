from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('',home,name='home'),
    path('regcust/',regCustView,name='register'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
    # path('regsell/',regSellView),
]
