from django.shortcuts import render,HttpResponse
from store.models import Cart, Products

# Create your views here.
def details(req,id):
    product_obj2=Products.objects.get(id=id)
    return render(req,'detail.html',{'product_obj2':product_obj2})

def addCart(req,id):
    pro=Products.objects.get(pk=id)
    obj=Cart()
    obj.productid=pro
    obj.userid=req.user
    obj.save()
    return HttpResponse('item added to cart')
    