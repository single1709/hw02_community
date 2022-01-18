from django.shortcuts import render, get_object_or_404
from .models import Post, Group

FIRST_RECORD: int = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:FIRST_RECORD]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = "Записи сообщества"
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:FIRST_RECORD]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
