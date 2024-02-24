from django import forms
from .models import UpForm

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UpForm
        fields = ["title","tags", "image", "body"]