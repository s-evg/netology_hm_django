from django.http import (
    HttpResponseNotFound,
    HttpResponse
)
from django.shortcuts import render

from articles.models import *


def articles_list_view(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().prefetch_related('scopes').order_by('-published_at')
    context = {
        'object_list': object_list,
    }
    print(f'ВОТ ===>>> {object_list[2].scopes.all()[1].is_main}')

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)


def post_view(request, slug):
    template = 'articles/post.html'
    post = Article.objects.get(slug=slug)
    context = {
        'post': post,
    }

    return render(request, template, context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(
        '<h1>Страница не найдена</h1>'
    )
