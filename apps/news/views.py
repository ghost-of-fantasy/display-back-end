from django.shortcuts import render, get_object_or_404
from apps.news.models import Article


# Create your views here.

def article_list(request):
    articles = Article.objects.get_queryset().filter(status='published')
    return render(request, 'news/article/list.html', {'articles': articles})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'news/article/detail.html', {'article': article})
