from datetime import datetime

import timeago
from django.db import models


class Thought(models.Model):
    thought = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_time_ago(self):
        return timeago.format(self.created_at.replace(tzinfo=None), datetime.utcnow(), 'zh_CH')
