from django.db import models

class Songs(models.Model):
        song_title = models.CharField(max_length=100)
        ref = models.CharField(max_length=1000)
        genre = models.CharField(max_length=100)
        artist = models.CharField(max_length=100)
        lang = models.CharField(max_length=100)
        album = models.CharField(max_length=1000)

        def __str__(self):
            return (self.song_title + " " + self.song + "mins long " + self.ref)


