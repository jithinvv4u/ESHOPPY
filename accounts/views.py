from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .forms import *
from django.contrib.auth import authenticate,login,logout
from store.models import Products
# from django.contrib import messages

# Create your views here.
def home(req):
    context={}
    context['product_obj']=Products.objects.all()
    return render(req,'index.html',context)

def regCustView(req):
    context={}
    context['form']=RegCustForm()
    if req.method=='GET':
        return render(req,'reg_cust.html',context)
    elif req.method=='POST':
        form=RegCustForm(req.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse("ok")
            # messages.success(req,"congratulation! Registration Successfull")
        else:
            return HttpResponse("not valid")

def loginView(req):
    if req.method=='GET':
        context={}
        context['form']=AuthenticationForm()
        return render(req,'login_cust.html',context)
    elif req.method=='POST':
        form=AuthenticationForm(request=req,data=req.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            pwd=form.cleaned_data['password']
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(req,user)
                return HttpResponse('success')
            else:
                return HttpResponse('failed')
        else:
            return HttpResponse('not valid')

def logoutView(req):
    logout(req)
    return redirect('login')

