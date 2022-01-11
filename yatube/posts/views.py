from django.shortcuts import render, get_object_or_404
from .models import Post, Group

LAST_LINES: int = 10


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:LAST_LINES]
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, template, context)


# Страница с группами
def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group}'
    posts = Post.objects.filter(group=group)[:LAST_LINES]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
