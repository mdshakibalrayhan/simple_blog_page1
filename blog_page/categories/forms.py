from django import forms

from .models import Category

class CategoryrForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
