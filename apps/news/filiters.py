import django_filters
from django.db.models import Q

from .models import Article


class ArticleFiliter(django_filters.rest_framework.FilterSet):
    """文章的过滤类"""

    id = django_filters.CharFilter(field_name='id')
    website_name = django_filters.CharFilter(field_name='website_name')
    url = django_filters.CharFilter(field_name='url')
    title = django_filters.CharFilter(field_name='title')
    content = django_filters.CharFilter(field_name='content')
    category = django_filters.CharFilter(method='top_category_filter', field_name='category')

    class Meta:
        model = Article
        fields = ['id', 'website_name', 'url', 'title', 'content', 'category']

    # 查找指定分类下的所有图书`
    def top_category_filter(self, queryset, name, value):
        print(queryset)
        return queryset.filter(Q(category__name=value))
