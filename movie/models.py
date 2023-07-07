# movie/models.py

from django.db import models
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=200)
    introduction = models.TextField()
    cast = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    director = models.CharField(max_length=40)
    on_showing = models.BooleanField(default=False)
    ticketing = models.URLField(blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='write_movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    hits = models.PositiveIntegerField(default= 0)
    score = models.FloatField(null = True)
    poster = models.URLField(blank=True, null=True)

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

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name= 'movie_expert_reviews')

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_expert_reviews')

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
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_general_reviews')

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_general_reviews')



