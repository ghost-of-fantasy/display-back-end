import django_filters
from django.db.models import Q
from taggit.models import Tag
from .models import Article


class ArticleFiliter(django_filters.rest_framework.FilterSet):
    """文章的过滤类"""

    id = django_filters.CharFilter(field_name='id')
    website_name = django_filters.CharFilter(field_name='website_name')
    title = django_filters.CharFilter(field_name='title')

    tags = django_filters.CharFilter(method='tags_filter', field_name='tags')

    class Meta:
        model = Article
        fields = ['id', 'website_name', 'title', 'tags']

    # 查找指定分类下的所有图书
    def tags_filter(self, queryset, name, value):
        tag = Tag.objects.get(id=value)
        return queryset.filter(tags__in=[tag])



