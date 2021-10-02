from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
class RegCustForm(UserCreationForm):

    class Meta:
        model=Customer
        fields={'username','email','phone','password1','password2',}

# class RegSellForm(UserCreationForm):

#     class Meta:
#         model=Seller
#         fields={'username','email','phone','password1','password2',}
