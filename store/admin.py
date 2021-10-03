from django.contrib import admin
from store.models import Products
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','description','image')
    search_fields=('name',)
admin.site.register(Products,ProductAdmin)
