from django.shortcuts import render, get_object_or_404
from .models import Post, Group

TOP_LINES_RESULT_QUERY: int = 10


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:TOP_LINES_RESULT_QUERY]
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group}'
#    posts = Post.objects.filter(group=group)[:TOP_LINES_RESULT_QUERY]
    posts = group.group_posts.all()[:TOP_LINES_RESULT_QUERY]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
