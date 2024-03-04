from django import forms
from .models import bodyflex_memebers
class bodyflex_form(forms.ModelForm):
    class Meta:
        model = bodyflex_memebers
        fields = "__all__"