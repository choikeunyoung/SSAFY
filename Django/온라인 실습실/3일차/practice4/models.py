from django.db import models

class Practice4_Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=10)
    director = models.CharField(max_length=20, default="Unknow")
    
    def __str__(self):
        answer = str(self.pk) + "번글 - " + str(self.title) + ": (" + str(self.genre) + ")"
        return answer