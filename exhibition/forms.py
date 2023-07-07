# exhibition/forms.py

from django import forms
from .models import Exhibition, Expert_review, General_review

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = ('title', 'schedule', 'introduction', 'artist', 'locations', 'ticketing', 'poster',)


class Expert_reviewForm(forms.ModelForm):
    class Meta:
        model=Expert_review
        fields = ('content', 'score', )

class General_reviewForm(forms.ModelForm):
    class Meta:
        model=General_review
        fields = ('content', 'score',)