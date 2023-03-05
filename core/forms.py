from django import forms
from .models import UserProfile

class UserProfileClass(forms.ModelForm):
class Meta:
    model = UserProfile
    fields = ['username', 'email', 'password1', 'password2']
    labels = {

    }