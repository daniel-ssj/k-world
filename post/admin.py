from django.contrib import admin

from .models import Comment, Thought

admin.site.register(Thought)
admin.site.register(Comment)
