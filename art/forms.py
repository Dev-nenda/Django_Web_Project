from django import forms
from .models import Art, Comment
from ckeditor.widgets import CKEditorWidget

class ArtForm(forms.ModelForm):
    title = forms.CharField(
        min_length= 1,
        max_length= 200,
    )

    content =  content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Art
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    
    content = forms.CharField(
        min_length=2,
        max_length=200,
    )

    class Meta:
        model = Comment
        fields = ('content',)