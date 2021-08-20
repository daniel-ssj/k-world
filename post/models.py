from django.db import models

from time import time
from random import randint


class Thought(models.Model):
    thought = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
