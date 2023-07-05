from django import forms
from .models import Moviecolumn, Comment

class MoviecolumnForm(forms.ModelForm):
    class Meta:
        model = Moviecolumn
        fields =('title', 'content',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )