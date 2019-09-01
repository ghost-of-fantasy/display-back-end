import django_filters
from taggit.models import Tag
from .models import UserComment


class CommentFiliter(django_filters.rest_framework.FilterSet):
    """文章的过滤类"""

    article = django_filters.CharFilter(field_name='article')

    class Meta:
        model = UserComment
        fields = ['article']
