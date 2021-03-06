from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

from user.models import Profile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
# __all__ untuk semua fiels
    class Meta:
        model = User
        fields = ['username','email','password','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']