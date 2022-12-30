from django import forms

class FormTrailers(forms.Form):
    title = forms.CharField()
    category = forms.CharField()
    year = forms.IntegerField()
    director = forms.CharField()
    actors = forms.CharField()
    review = forms.IntegerField()
    image_link = forms.CharField()
    youtune_link = forms.CharField()