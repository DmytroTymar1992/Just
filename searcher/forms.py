from django import forms
from .models import Resume
from main.models import User

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = []

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'date_of_birth')
    