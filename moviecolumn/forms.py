from django import forms
from .models import Moviecolumn, Comment
from ckeditor.widgets import CKEditorWidget

class MoviecolumnForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Moviecolumn
        fields =('title', 'content', 'cover')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )