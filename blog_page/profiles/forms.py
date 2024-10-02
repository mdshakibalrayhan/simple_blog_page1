from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # Use 'model' instead of 'models'
        fields = '__all__'  # This will include all fields in the form
