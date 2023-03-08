from django.contrib.auth.forms import UserChangeForm
from django.contrib.gis import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('home_address', 'phone_number', 'location')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('home_address', 'phone_number', 'location')
