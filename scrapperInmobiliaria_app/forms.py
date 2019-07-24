from django import forms


class ScrapperForm(forms.Form):
    email = forms.EmailField()
    sector = forms.CharField(max_length=45)
