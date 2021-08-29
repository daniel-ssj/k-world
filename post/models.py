from datetime import datetime

import timeago
from django.contrib.auth.models import User
from django.db import models


class Thought(models.Model):
    thought = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thoughts')

    def get_time_ago(self):
        return timeago.format(self.created_at.replace(tzinfo=None), datetime.utcnow())

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def get_time_ago(self):
        return timeago.format(self.created_at.replace(tzinfo=None), datetime.utcnow())
