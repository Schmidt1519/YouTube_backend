from django.db import models

# Create your models here.

class Comment(models.Model):
    video_id = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=250)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=250)
