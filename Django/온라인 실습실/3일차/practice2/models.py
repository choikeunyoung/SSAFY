from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=10)
    
    def __str__(self):
        answer = str(self.pk) + "번글 - " + str(self.title) + ": (" + str(self.genre) + ")"
        return answer