from django.db import models
from django.conf import settings

class Exhibition(models.Model):
    title = models.CharField(max_length=100)
    
    schedule = models.CharField(max_length=50)

    introduction = models.TextField()

    artist = models.CharField(max_length=30)

    locations = models.CharField(max_length=100)

    ticketing = models.URLField(blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exhibitions')

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_exhibitions')


class Expert_review(models.Model):

    SCORE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    content = models.CharField(max_length=100)

    score = models.IntegerField(choices=SCORE_CHOICES)
    

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expert_reviews')

    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, related_name='expert_reviews')

class General_review(models.Model):

    SCORE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    content = models.CharField(max_length=100)

    score = models.IntegerField(choices=SCORE_CHOICES)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='general_reviews')

    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, related_name='general_reviews')
