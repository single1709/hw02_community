from django.shortcuts import render, get_object_or_404
from .models import Post, Group

FIRST_RECORD: int = 10

def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:FIRST_RECORD]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:FIRST_RECORD]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
