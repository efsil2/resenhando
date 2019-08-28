import site
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

generos = [{'ação':'ação','animação':'animação','comedia':'comedia','drama':'drama','ficção científica':'ficção científica','infantil':'infantil','nacional':'nacional','suspense':'suspense','terror':'terror','outros':'outros'}]
classificação = [{'livre':'livre','+12':'+12','+10':'+10','+14':'+14','+16':'+16','+18':'+18'}]

class Films(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    premiere = models.DateTimeField()
    directors = models.CharField(max_length=100)
    starring = models.CharField(max_length=200)
    genre = models.CharField(max_length=20)
    parental_rating = models.CharField(max_length=5)
    production = models.CharField(max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
