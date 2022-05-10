from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    root_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    video_caption = models.CharField(max_length=500)
    video_file = models.FileField(upload_to='uploaded_videos', null=True, blank=True)
    video_url = models.CharField(max_length=1000, null=True, blank=True)
    video_tags = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.video_caption
