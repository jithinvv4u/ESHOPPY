from django.shortcuts import render

from store.models import Products

# Create your views here.
def details(req,id):
    product_obj2=Products.objects.get(id=id)
    return render(req,'detail.html',{'product_obj2':product_obj2})