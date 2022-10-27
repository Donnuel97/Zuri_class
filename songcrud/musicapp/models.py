from turtle import title
from django.db import models
from django.utils import timezone

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    
class Song(models.Model):
    artist = models.ForeignKey(Artiste,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField()
    likes = likes = models.ManyToManyField(Artiste, related_name = 'song_post')

    #this function helps to add the total number of likes on a post
    def total_likes(self):
        return self.likes.count()

class Lyric(models.Model):
    song = models.ForeignKey(Song,on_delete=models.CASCADE)
    content = models.TextField
   