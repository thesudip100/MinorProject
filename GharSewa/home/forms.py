from django import forms
from .models import userRegister,profRegister
 
# class userRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1','email','password2']


class userRegisterForm(forms.ModelForm):
    
    class Meta:
        model = userRegister
        fields = '__all__'

class profRegisterForm(forms.ModelForm):
    
    class Meta:
        model = userRegister
        fields = '__all__'