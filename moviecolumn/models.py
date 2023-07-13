from django.db import models
from django.conf import settings
from movie.models import Movie
from ckeditor_uploader.fields import RichTextUploadingField
class Moviecolumn(models.Model):
    title =  models.CharField(max_length=100)

    content = RichTextUploadingField(blank=True,null=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='moviecolumns')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moviecolumns', null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_moviecolumns')
    clipping_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='clipping_moviecolumns')
    hits = models.PositiveIntegerField(default= 0)
    cover = models.URLField(blank=True, null=True)
class Comment(models.Model):
    content = models.CharField(max_length=100)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='moviecolumn_comment')

    moviecolumn = models.ForeignKey(Moviecolumn, on_delete=models.CASCADE, related_name='comments')