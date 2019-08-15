import django_filters
from .models import Article


class ArticleFiliter(django_filters.rest_framework.FilterSet):
    """图片的过滤类"""

    id = django_filters.CharFilter(field_name='id')
    website_name = django_filters.CharFilter(field_name='website_name')
    url = django_filters.CharFilter(field_name='url')
    title = django_filters.CharFilter(field_name='title')
    content = django_filters.CharFilter(field_name='content')
    category = django_filters.CharFilter(field_name='category')

    class Meta:
        model = Article
        fields = ['id', 'website_name', 'url', 'title', 'content', 'category']