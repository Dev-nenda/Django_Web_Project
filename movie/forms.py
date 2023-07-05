from django import forms
from .models import Movie, Expert_review, General_review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('like_users', 'writer')

class Expert_reviewForm(forms.ModelForm):
    class Meta:
        model=Expert_review
        fields = ('content', 'score',)

class General_reviewForm(forms.ModelForm):
    class Meta:
        model=General_review
        fields = ('content', 'score',)