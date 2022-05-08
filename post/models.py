from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
