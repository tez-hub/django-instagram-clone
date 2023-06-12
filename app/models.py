from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.TextField()
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} at {self.timestamp}"
    

class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)
    expiration_timestamp = models.DateTimeField()

    def __str__(self):
        return f"Story by {self.user.username} at {self.timestamp}"

    def is_expired(self):
        return self.expiration_timestamp <= timezone.now()