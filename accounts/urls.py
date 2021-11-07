from django.contrib import admin
from django.urls import path
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name='home'),
    path('regcust/',regCustView,name='register'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
    # path('regsell/',regSellView),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

