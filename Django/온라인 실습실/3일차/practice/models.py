from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        answer = str(self.created_at.month)+"/"+str(self.created_at.day)+"에 생성된" + str(self.pk) + "번글 - " + str(self.title) + " : " + str(self.content)
        return answer