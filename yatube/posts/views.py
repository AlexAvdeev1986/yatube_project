from django.shortcuts import render, get_object_or_404
from .models import Post, Group

NUM_OF_PUBLICATIONS: int = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:NUM_OF_PUBLICATIONS]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_list(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:NUM_OF_PUBLICATIONS]
    context = {
        'text': slug,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
