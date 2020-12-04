from django import forms
from .models import Pet, Image

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)