import django_filters
from django.db.models import Q

from .models import Article, Comment


class ArticleFiliter(django_filters.rest_framework.FilterSet):
    """文章的过滤类"""

    id = django_filters.CharFilter(field_name='id')
    website_name = django_filters.CharFilter(field_name='website_name')
    title = django_filters.CharFilter(field_name='title')
    category = django_filters.CharFilter(field_name='category')

    # category = django_filters.CharFilter(method='top_category_filter', field_name='category')

    class Meta:
        model = Article
        fields = ['id', 'website_name', 'title', 'category']

    # 查找指定分类下的所有图书
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category__name=value))


class CommentFiliter(django_filters.rest_framework.FilterSet):
    """评论的过滤类"""

    id = django_filters.CharFilter(field_name='id')
    name = django_filters.CharFilter(field_name='name')
    article = django_filters.CharFilter(field_name='article')
    active = django_filters.BooleanFilter(field_name='active')

    # category = django_filters.CharFilter(method='top_category_filter', field_name='category')

    class Meta:
        model = Comment
        fields = ['id', 'name', 'article', 'active']

    # 查找指定分类下的所有图书`
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category__name=value))
