from django import forms

from .models import AnimeFile


class AnimeFileForm(forms.ModelForm):
    class Meta:
        model = AnimeFile

        fields = [

            'file'

        ]

        labels = {

            'file': 'File',

        }

        widgets = {

            'file': forms.ClearableFileInput(attrs={'multiple': True}),
        }
