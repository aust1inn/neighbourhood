from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']   
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class CreateHoodForm(forms.ModelForm):

	class Meta:
		model = Hood
		exclude = ['user','occupants_count']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','hood']    

class PostForm(forms.ModelForm):

	class Meta:
		model = Posts
		fields = ['title','content']            