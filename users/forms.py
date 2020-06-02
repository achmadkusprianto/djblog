# untuk menyempurnakan form di template yang digunakan
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# untuk menambahkan field pada register 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# menampilkan form2 register di profil
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

# menampilkan menu update image di profil
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['images']
