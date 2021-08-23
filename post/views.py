from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from post.models import Thought


def latest_thoughts_view(request):
    thought = Thought.objects.first()
    print(thought.thought)
    context = {
        'thought': thought
    }
    return render(request, 'post/thoughts.html', context)

def thought_create_view(request):
    thoughts = Thought.objects.all().order_by('-created_at')

    print(request.method == 'POST')

    if(request.method == 'POST'):
        thought = request.POST.get('thought')
        Thought.objects.create(thought=thought)

        return redirect("/")
    
    context = {
        'thoughts': thoughts
    }

    return render(request, 'post/create.html', context)
