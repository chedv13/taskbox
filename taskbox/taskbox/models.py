from django.db import models
from taskbox.users.models import User


class Task(models.Model):
    text = models.TextField(default='')
    closed = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
