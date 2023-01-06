from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    def __str__(self):
        return f"{self.title}"