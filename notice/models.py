from django.db import models
from django.conf import settings

class Notice(models.Model):
    title = models.CharField(max_length=100)

    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notices')