from post.models import Thought
from django.shortcuts import render

def thoughts(request):
    thought = Thought.objects.first()
    print(thought.thought)
    context = {
        'thought': thought
    }
    return render(request, 'post/post.html', context)