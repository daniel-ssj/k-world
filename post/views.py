from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from post.models import Thought


@login_required
def thought_create_view(request):
    if(request.method == 'POST'):
        thought: str = request.POST.get('thought')

        Thought.objects.create(thought=thought, author=request.user)

        return redirect("/")


@login_required
def thought_delete_view(request, id):
    if(request.method == 'GET'):
        thought: Thought = Thought.objects.get(pk=id)
        thought.delete()

@login_required
def index_view(request):
    thoughts_list = Thought.objects.all().order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(thoughts_list, 10)

    try:
        thoughts = paginator.page(page)
    except PageNotAnInteger:
        thoughts = paginator.page(1)
    except EmptyPage:
        thoughts = paginator.page(paginator.num_pages)

    context = {'thoughts': thoughts}

    if int(page) > 1:
        return render(request, 'post/thoughts.html', context)

    return render(request, 'post/index.html', context)
