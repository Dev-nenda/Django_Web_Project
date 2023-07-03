# art/models.py

from django.db import models
from django.conf import settings

class Art(models.Model):
    title = models.CharField(max_length=100)

    content = models.TextField()

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='arts')

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_arts')

    clipping_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='clipping_arts')


class Comment(models.Model):
    content =models.CharField(max_length=100)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    
    art = models.ForeignKey(Art, on_delete=models.CASCADE, related_name='comments')